class Building(object):
    def __init__(self):
        self.customer_list = []
        
        num_of_floors = input("input number of floors: ")
        while not num_of_floors.isdigit():
            print("Wrong Input!")
            num_of_floors = input("input num_of_floors: ")
        self.num_of_floors = num_of_floors
    
        num_of_customers = input("input number of customers: ")
        while not num_of_customers.isdigit():
            print("Wrong Input!")
            num_of_customers = input("input num_of_customers: ")
        self.num_of_customers = num_of_customers
        
        
        for i in range(int(self.num_of_customers)):
            c = Customer(i+1, int(self.num_of_floors))
            self.customer_list.append(c)

    def check_all_finished(self):
        for x in self.customer_list:
            if x.get_finished() == False:
                return False
        return True
    

    def run(self):
        for c in self.customer_list:
            # 이미 이용해서 끝난 customer는 다시 태우지 말아야 함
            if (c.get_finished()== False and (c.get_cur_floor() == self.elevator.get_cur_floor())):
                print("Customer {} -> Elevator".format(c.ID))
                c.set_in_elevator(True)
                self.elevator.register_customer(c)

            # 엘리베이터에 있었다면 내려야함. 없었다면 내리면 안됨
            if (c.get_in_elevator() and c.get_dst_floor() == self.elevator.get_cur_floor()):
                print("Customer {} -> Destination Floor".format(c.ID))
                c.set_finished(True)
                c.set_in_elevator(False)
                self.elevator.cancel_customer(c)

        self.output()

        
        
    def output(self):
        print()
        print("Elevator current floor: ",self.elevator.cur_floor, end='\t')
        print("Elevator's Direction: ", self.elevator.direction)
        print("Customers:")
        for x in self.customer_list:
            print("\tCustomer {}\tcurrent floor : {}\tdestination floor: {}".format(x.ID,x.cur_floor, x.dst_floor))
            print("\t\t\tin Elevator : {} \t isFinished: {}".format(x.in_elevator, x.finished))
        print()
        print("->"*35)
        # 모든 승객이 이용했다면 True를 리턴하도록 한다. 
        if self.check_all_finished() :
            return True
        else: False

        Elevator.move()

# ----------------------------------------------------- 
class Elevator(object):
    def __init__(self, num_of_floors):
        self.num_of_floors = int(num_of_floors)
        self.register_list = []

        cur_floor = random.randint(1, num_of_floors)
        self.cur_floor = cur_floor

        if self.cur_floor == self.num_of_floors:
            direction = 'down'
        elif self.cur_floor == 1:
            direction = 'up'
        else:
            direction = random.choice(["up","down"])

        self.direction = direction
            

    def move(self):
        old_floor = self.cur_floor
        if self.direction == "up":
            if self.cur_floor == num_of_floors:
                print("The Elevator is on the Top Floor Now")
                self.direction = "down"
                self.cur_floor -=1
            else: self.cur_floor += 1
        else:
            if self.cur_floor == 1:
                print("The Elevator is on the Bottom Floor Now")
                self.direction = "up"
                self.cur_floor += 1
            else: self.cur_floor -= 1
        print("Elevator : {} -> {}".format(old_floor , self.cur_floor))
            

    def get_cur_floor(self):
        return self.cur_floor

    def register_customer(self,customer):
        self.register_list.append(customer)
    def cancel_customer(self, customer):
        self.register_list.remove(customer)
# -----------------------------------------------------        
class Customer(object):
    def __init__(self, ID, num_of_floors):
        self.ID = ID 

        #customer의 cur_floor, dst_floor
        cur_floor = random.randint(1, num_of_floors)
        self.cur_floor = cur_floor

        dst_floor = random.randint(1, num_of_floors)
        while cur_floor == dst_floor:
            dst_floor = random.randint(1, num_of_floors)
        self.dst_floor = dst_floor
   
    
    def set_in_elevator(self, in_elevator):
        self.in_elevator = in_elevator
    def get_in_elevator(self):
        return self.in_elevator
    
    def set_finished(self, finished):
        self.finished = finished
    def get_finished(self):
        return self.finished   
# ----------------------------------------------------- 
import random

test = Building()
test.run()

      
