from functools import reduce
import os


class HexRecord(object):
    RECORD_TYPE = {'00': 'DataRecord',
                   '01': 'EndOfFileRecord',
                   '02': 'ExtendedSegmentAddressRecord',
                   '03': 'StartSegmentAddressRecord',
                   '04': 'ExtendedLinearAddressRecord',
                   '05': 'StartLinearAddressRecord'}
    record_test = ':02000004800278\n'

    def __init__(self, record=':02000004800278\n'):
        self.record = record[1:-1]  # 去除冒号和换行符的未经分割的原始record
        self.record_str = [self.record[i:i + 2] for i in range(0, len(self.record), 2)]  # 以8位形式分割且为字符串类型
        self.record_num = [int(self.record[i:i + 2], 16) for i in range(0, len(self.record), 2)]  # 以8位形式分割且为数值类型

        self.record_type = self.RECORD_TYPE[self.record_str[3]]
        self.record_addr = '0x0000'
        self.record_data = self.record_str[4:-1]
        self.record_len = self.record_num[0]

        self.record_checksum = int(self.record_str[-1], 16)
        self.record_validity = self.checksum()

        if self.record_type == 'DataRecord':
            self.record_addr = '0x' + ''.join(self.record_str[1:3])
            self.record_data = self.record_str[4:-1]

        elif self.record_type == 'EndOfFileRecord':
            # 文件结束记录不做任何处理
            pass

        elif self.record_type == 'ExtendedSegmentAddressRecord':
            # 暂不清楚02类型Record的作用
            pass

        elif self.record_type == 'StartSegmentAddressRecord':
            # 暂不清楚03类型Record的作用
            pass

        elif self.record_type == 'ExtendedLinearAddressRecord':
            self.record_addr = '0x' + ''.join(self.record_str[4:-1])

        elif self.record_type == 'StartLinearAddressRecord':
            self.record_addr = '0x' + ''.join(self.record_str[4:-1])
            pass
        else:
            print('不正常的Record类型！')

        pass

    def checksum(self):
        checksum = (0x100 - (reduce(lambda x, y: x + y, self.record_num[:-1]) % 256)) % 256

        if checksum == self.record_checksum:  # check if sum calculated is equal to checksum byte in hex file
            return True
        else:
            return False

    def __str__(self):
        return f'Record type: {self.record_type}, Record data length: {self.record_len}H, Record data: {self.record_data}'


class MyHex(object):
    class HexRecords32BytesIterator(list):
        def __init__(self):
            self.container = []
            self.index = 0

        def __iadd__(self, other):
            self.container += other
            return self

        def __next__(self):
            if self.index < len(self.container):
                result = self.container[self.index:self.index + 32]
                self.index += 32
                return result
            else:
                self.index = 0
                raise StopIteration

        def __iter__(self):
            return self

        def __len__(self):
            return len(self.container)

        def distroyed(self):
            del self.container
            self.index = -1

    def __init__(self, file_path):
        self.file_path = file_path
        self.hex_file_content = None
        self.hex_records = []
        self.addr_start = None
        self.addr_end = None
        self.hex_preprocess()  # 对hex文件内容进行前处理
        self.total_size = os.path.getsize(self.file_path)
        self.total_record = len(self.hex_records)
        self.hex_records_32Bytes = self._hex_reformat_to_32bytes()  # 返回值为dict
        self.hex_records_32Bytes_len = reduce(lambda x, y: x + y, [len(i)for i in self.hex_records_32Bytes.values()])
        pass

    def hex_preprocess(self):
        print('Hex File PreProcessing Start...')
        with open(self.file_path, 'r') as f:
            self.hex_file_content = f.readlines()
            for r in self.hex_file_content:
                record = HexRecord(r)
                self.hex_records.append(record)
                # print(record)

        temp = list(filter(lambda r: r.record_type == 'ExtendedLinearAddressRecord', self.hex_records))
        self.addr_start = temp[0].record_addr + self.hex_records[self.hex_records.index(temp[0]) + 1].record_addr[2:]
        self.addr_end = temp[0].record_addr + self.hex_records[self.hex_records.index(temp[1]) - 1].record_addr[2:]
        self.addr_end = hex(
            int(self.addr_end, 16) + self.hex_records[self.hex_records.index(temp[1]) - 1].record_len - 1)
        print('Hex File PreProcessing End...')

    def _hex_reformat_to_32bytes(self):
        # 将原hex文件转换为按32byte分割成块的数据，供下位机刷写FLASH
        all_record_datas = {}

        for i, r in enumerate(self.hex_records):  # type: HexRecord
            if r.record_type == 'ExtendedLinearAddressRecord':
                if r.record_addr[2] == '8':
                    # 判断地址是否在范围，并将0x8000转为0xA000范围段，否则抛出异常
                    r.record_addr = r.record_addr[:2] + 'A' + r.record_addr[3:]
                    current_extended_linear_addr = r.record_addr
                    next_record_addr = self.hex_records[i+1].record_addr
                    current_start_addr = r.record_addr + next_record_addr[2:]
                    all_record_datas[current_start_addr] = self.HexRecords32BytesIterator()
                    new_extended_linear_flag = 1
                else:
                    raise ValueError('地址不在指定范围，TC234 PFlash范围为：0xA000 0000 - 0xA01F FFFF.')
            elif r.record_type == 'DataRecord':
                if int(current_extended_linear_addr + r.record_addr[2:], 16) - int(current_start_addr, 16) \
                        == len(all_record_datas[current_start_addr]):
                    # 如果两DataRecord之间地址连续
                    all_record_datas[current_start_addr] += r.record_data
                    pass

                else:
                    # 两DataRecord之间地址不连续
                    # fill_0xff_num = int(r.record_addr, 16) - len(all_record_datas[current_start_addr])  # 这条代码有错
                    fill_0xff_num = int(current_extended_linear_addr + r.record_addr[2:], 16) \
                                    - int(current_start_addr, 16) - len(all_record_datas[current_start_addr])
                    all_record_datas[current_start_addr] += ['FF' for i in range(fill_0xff_num)]
                    all_record_datas[current_start_addr] += r.record_data
                    pass
                pass
            else:
                pass

        for v in all_record_datas.values():
            # 最后一段补全至32byte
            if len(v) % 32 != 0:
                n = 32 - len(v) % 32
                v += ['FF' for i in range(n)]
        return all_record_datas

    def hex_print_to_txt(self):
        pass

    def __str__(self):
        return f'\n' \
               f'*Hex file information:\n' \
               f'*Hex name: {os.path.basename(self.file_path)}\n' \
               f'*Hex path: {os.path.abspath(self.file_path)}\n' \
               f'*Address start: {self.addr_start}\n' \
               f'*Address end: {self.addr_end}\n' \
               f'*Total record: {self.total_record}\n' \
               f'*Total size: {self.total_size}' \
               f'\n'


if __name__ == '__main__':
    hex_file = './Intron_App_TC234L.hex'
    myhex = MyHex(hex_file)

    for v in myhex.hex_records_32Bytes.values():
        for e in v:
            print(e)
    pass
    # print(myhex.hex_records[0])
