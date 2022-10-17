import json
import csv


class PhoneBook:
    def __init__(self, file_name='db.json'):
        self.file_name = file_name
        try:
            with open(self.file_name) as db:
                self.data = json.load(db)
        except:
            self.data = []
            self.save()

    def __repr__(self):
        return json.dumps(self.data, ensure_ascii=False, indent=4)

    def save(self):
        with open(self.file_name, 'w', encoding='utf8') as db:
            json.dump(self.data, db, ensure_ascii=False, indent=4)

    def purge(self):
        self.data = []
        self.save()

    def add(self, record):
        if self.validate_record(record):
            self.data.append(record)
            self.save()
            return True
        return False

    def delete(self, index):
        if len(self.data) <= index:
            return False
        self.data.pop(index)
        self.save()
        return True

    def get(self, index, print_now=True):
        if len(self.data) <= index:
            return {}
        if print_now:
            self.print([(index, self.data[index])])
        return self.data[index]

    def get_all(self, print_now=True):
        if print_now:
            self.print()
        return self.data

    def find(self, field, query, print_now=True):
        result = list(filter(lambda e: query.lower()
                      in e[1][field].lower(), enumerate(self.data)))
        if print_now:
            self.print(result)
        return [e[1] for e in result]

    def print(self, data=None, print_now=True):
        if data == None:
            data = enumerate(self.data)
        result = [f"{'№':<5}{'ФИО': <50}Телефон"]

        result += list(map(lambda record:
                           f"{record[0]:<5}{record[1]['name']: <50}{record[1]['phone']}", data))
        if print_now:
            for record in result:
                print(record)
        return result

    def export(self, file_name, type='json'):
        with open(file_name, 'w', encoding='utf8') as export_file:
            if type == 'json':
                json.dump(self.data, export_file, ensure_ascii=False, indent=4)
            elif type == 'csv':
                writer = csv.DictWriter(
                    export_file, fieldnames=['name', 'phone'])
                writer.writeheader()
                writer.writerows(self.data)
            else:
                print('Неправильный тип файла')

    def load(self, file_name, type='json'):
        with open(file_name, encoding='utf8') as import_file:
            if type == 'json':
                 self.data = json.load(import_file)
            # elif type == 'csv':
            #     writer = csv.DictWriter(
            #         export_file, fieldnames=['name', 'phone'])
            #     writer.writeheader()
            #     writer.writerows(self.data)
            else:
                print('Неправильный тип файла')

    def validate_record(self, record):
        if not isinstance(record, dict):
            return False
        if not ("name" and "phone" in record):
            return False
        return True

    def validate(self, data):
        if data == None:
            return False
        if not isinstance(data, list):
            return False
        for record in data:
            if not self.validate_record(record):
                return False
        return True
    