from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
    
class Name(Field):
    def __init__(self, name):
        super().__init__(name)
    

class Phone(Field):
    phone_len = 10

    def __init__(self, phone):
        validated_phone = self.validate(phone)
        super().__init__(validated_phone)
        
    def validate(self, phone):
        try:
            int(phone) and len(phone) == Phone.phone_len
            return phone
        except:
            raise ValueError(f"The correct phone number must contain {Phone.phone_len} numbers") 


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        try:
            _phone = Phone(phone)
            self.phones.append(_phone)
        except ValueError as e:
            print(e)
            return None

    def remove_phone(self, phone):
        for _phone in self.phones:
            if(_phone.value == phone):
                return self.phones.remove(_phone)
        return "Phone not found"
    
    def edit_phone(self, phone, new_phone):
        for i in range(len(self.phones)):
            if(self.phones[i].value == phone):
                try:
                    _new_phone = Phone(new_phone)
                    self.phones[i] = _new_phone
                    return "Phone changed successfully"
                except ValueError as e:
                    print(e)
    
    def find_phone(self, phone):
        for _phone in self.phones:
            if(_phone.value == phone):
                return _phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"



class AddressBook(UserDict):
    def add_record(self, data):
        self.data[data.name] = data
        return f"\"{data.name}\" was added"
    
    def find(self, name):
        for key in self.data.keys():
            if key.value == name:
                return self.data[key]
        return f"\"{name}\" not found"
        
    def delete(self, name):
        for _name in self.data:
            if _name.value == name:
                return self.data.pop(_name)
        return f"\"{name}\" not found"
        