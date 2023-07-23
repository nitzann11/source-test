class Owner:
    def __init__(self,name:str="default name",last_name:str="default last name",phone:str="default phone number",country:str="defult country",city:str="default city"
                ,street:str="default street",house_num:str="default house number"):
        self.name=name
        self.last_name=last_name
        self.phone=phone
        self.country=country
        self.city=city
        self.street=street
        self.house_num=house_num
        
    def __str__(self) -> str:
        return f'{self.name}\t{self.last_name}\t{self.phone}\t{self.country}\t{self.city}\t{self.street}\t{self.house_num}'
    