

class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__expense = 0 


    def get_category_name(self):
        return self.__category_name

    def set_category_name(self, category_name):
        if isinstance(category_name, str) and category_name.strip():
            self.__category_name = category_name
        else:
            raise ValueError("category name must be in letters")
        
    def get_allocated_budget(self):
        return self.__allocated_budget
    
    def set_allocated_budget(self, allocated_budget):
        if isinstance(allocated_budget, (int, float)) and allocated_budget > 0:
            self.__allocated_budget = allocated_budget
        else:
            raise ValueError("allocated budget must be positive number")
        
    def add_expense(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            if self.__expense + amount <= self.__allocated_budget:
                self.__expense += amount
            else:
                raise ValueError("expense over allocated amount")
        else:
            raise ValueError("expense amount must be a positive number")
        
    def display_category_summary(self):
        remaining_budget = self.__allocated_budget - self.__expense
        print(f"category : {self.__category_name}")
        print(f"allocated budget: ${self.__allocated_budget}")
        print(f"expenses: ${self.__expense}")
        print(f"remaining budget ${remaining_budget}")


food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()