import csv

class System:
    def __init__(self):
        self.sensors_list = list()
        self.sensor_mapping_list = list()
        self.master_node_list = list()
        
    def config_system(self, file):
        data_file = open(file, 'r')
        reader = csv.DictReader(data_file)
        for row in reader:
            node_id = row['Node ID']
            type = row['Type']
            master_node_id = row['Master Node ID']
            
            if type == 'Master':
                self.master_node_list.append(int(master_node_id))
            elif type == "Sensor":
                self.sensors_list.append(int(node_id))
                self.sensor_mapping_list.append(int(master_node_id))
                
        
    def SensorAssignedCount(self, mapping_list, l, r, OverloadSensor):
        count = 0
        for i in range(l, r+1):
            if (mapping_list[i] == OverloadSensor): 
                count +=  1
        return count
    
    def OverloadNodeHelper(self, l, r):
        if l == r:
            return self.master_node_list[l]
        mid = (l + r) // 2
        left_overloaded = self.SensorAssignedCount(l, mid, self.master_node_list[mid])
        right_overloaded = self.SensorAssignedCount(mid + 1, r, self.master_node_list[mid])
        if left_overloaded:
            return self.OverloadNodeHelper(l, mid)
        elif right_overloaded:
            return self.OverloadNodeHelper(mid + 1, r)
        return None
        
    def getOverloadedNode(self):
        return self.OverloadNodeHelper(0, len(self.sensor_mapping_list)-1)
    
    def getPotentialOverloadNode(self):
        n = len(self.sensors_list)
        potential_overloaded_nodes = []

        for master_node in self.master_node_list:
            sensor_count = self.SensorAssignedCount(0, n - 1, master_node)
            if n // 3 <= sensor_count < n // 2:
                potential_overloaded_nodes.append(master_node)

        return potential_overloaded_nodes
    
if __name__ == "__main__":
    test_system1 = System()
    
    test_system1.config_system('app_data1.csv')
    
    print("Overloded Master Node : ", test_system1.getOverloadedNode())
    
    print("Partially Overloaded Master Node : ", test_system1.getPotentialOverloadNode())

    test_system2 = System()
    
    test_system2.config_system('app_data2.csv')
    
    print("Overloded Master Node : ", test_system2.getOverloadedNode())
    
    print("Partially Overloaded Master Node : ", test_system2.getPotentialOverloadNode())

    test_system3 = System()

    test_system3.config_system('app_data3.csv')
    
    print("Overloded Master Node : ", test_system3.getOverloadedNode())
    
    print("Partially Overloaded Master Node : ", test_system3.getPotentialOverloadNode())

    test_system4 = System()

    test_system4.config_system('app_data4.csv')
    
    print("Overloded Master Node : ", test_system4.getOverloadedNode())
    
    print("Partially Overloaded Master Node : ", test_system4.getPotentialOverloadNode())
