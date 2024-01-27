import re
import sys


class cpf_validator:
    def __init__(self):
        self.str_patern = re.compile("[0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}-?[0-9]{2}")
        self.PENULT_DIGIT_POS = 9
        self.LAST_DIGIT_POS = 10
    
    def is_valid(self, cpf:str) -> bool:
        if not self.str_patern.match(cpf):
            return False
        
        cpf = self.__normalize_cpf(cpf)
        
        return self.__validate_digit(cpf, self.PENULT_DIGIT_POS) and self.__validate_digit(cpf, self.LAST_DIGIT_POS)
    
    def __validate_digit(self, cpf:str, pos:int) -> bool:
        sum = 0
        counter = pos + 1
        cpf_digit = int(cpf[pos])
        
        
        for digit in cpf[:pos]:
            sum += int(digit) * counter
            counter -= 1
        
        valid_digit = 0 if (mod:= sum % 11) < 2 else 11 - mod  
        return valid_digit == cpf_digit
        
    def __normalize_cpf(self, cpf:str) -> str:
        return cpf.replace('.', '').replace('-', '')
        
    
def main():
    if len(sys.argv) < 2:
        print("Forneça um (ou mais) CPF para a validação.")
        print("Exemplos:\n\tpython cpf_validator.py 123.456.789-09")
        print("\tou")
        print("\tpython cpf_validator.py cpf-1 cpf-2 ... cpf-n")
        sys.exit(1)
    
    validator = cpf_validator()
    
    for cpf in sys.argv[1:]:
        if validator.is_valid(cpf):
            print(f"O cpf: '{cpf}' é válido")
        else:
            print(f"O cpf: '{cpf}' é inválido")

if __name__ == "__main__":
    main()