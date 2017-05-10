



class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

# Methods for setting and getting the data
	def set_data(self, data):
		self.data = data
	
	def get_data(self):
		return self.data

#Method for setting the next node and getting the next node of data
	def set_next(self, next):
		self.next = next

	def get_next(self, next):
		return self.next

# Method for check if their is next node, it will return True if their is node and will return false if their is not a node
	def has_next(self):
		return self.next != None


# Class for defining the linked List
class LinkedList(object):

# Initialised the list with length and head
	def __init__(self):
		self.head = None
		self.length = 0

# Check if the node exist or not, if it does not exist then create first node or else add the new node to last.
	def add_node(self, node):
		if self.length == 0:
			self.addbeg(node)
		else:
			self.addlast(node)
	
# Method to add node in the begining assuming no node exist or even if the node exist we will change the head pointer.
	def add_beg(self, node):
		newnode = node
		newnode.next = self.head
		self.head = newnode
		self.length += 1


# Method to add a node after the node having a value data=data, the data of the new node is tha parameter we are passing as node. 
	def addaftervalue (self, data, node):
		newnode = node
		currentnode = self.head

		while currentnode != None or currentnode.data != data:
			if currentnode.data == data:
				newnode.next = currentnode.next
				currentnode.next = newnode
				self.length +=1
				return
			else:
				currentnode = currentnode.next
		
		print(" The data provided is not present")

# Method to add a node at a particular position
	def addatposition (self, pos, node):
		count = 0
		currentnode = self.head
		previousnode = self.head

		if pos > self.length or pos < 0:
			print("The position does not exit, Please enter valid position")
		else:
			while currentnode.next != None or count < pos:
				count +=1
				if count == pos:
					previousnode.next = node
					node.next = currentnode
					self.length += 1
					return
				else:
					previousnode = currentnode
					currentnode = currentnode.next

# Method to add a node at the end of the list
	def addLast(self, node):
		currentnode = self.head

		while currentnode.next != None:
			currentnode = currentnode.next
		
		newnode = node
		newnode.next = None
		currentnode.next = newnode
		self.length = self.length + 1

# Method to delete the first node of Linked List
	def deletebeg (self):
		if self.length == 0:
			print("The list is empty")
		else:
			self.head = self.head.next
			self.length -= 1

# Method to delete the last node of linked list
	def deletelast(self):
		if self.length == 0:
			print(" The list is empty")
		else:
			currentnode = self.head
			previousnode = self.head
			while currentnode.next != None:
				currentnode = currentnode.next
				previousnode = currentnode

			previousnode.next = None

			self.length -= 1

# Method to delete a node after the node having the given data	
	def deletevalue(self, pos):
		currentnode = self.head
		previousnode = self.head

		while currentnode != None or currentnode.data != data:
			if currentnode.data == data:
				previousnode.next = currentnode.next
				self.length -= 1
				return
			else:
				previousnode = currentnode
				currentnode = currentnode.next

		print("The data provided is not present")


# Method to delete the node at a particular position
	def deleteatposition(self, pos):
		count = 0
		currentnode = self.head
		previousnode = self.head

		if pos > self.length or pos < 0:
			print(" The position does not exist, please enter the valid position")
		elif pos == 1:
			self.deletebeg()
			self.length -= 1
		else:
			while currentnode.next != None or count < pos:
				count +=1
				if count == pos:
					previousnode.next = currentnode.next
					self.length -=1
					return
				else:
					previousnode = currentnode
					currentnode = currentnode.next

# returns the length of list

	def getlength(self):
		currentnode = self.head
		count = 0
		while currentnode.next != None:
			count +=1

		return count

# returns the first element of the list
	def getfirst(self):
		if self.length == 0:
			print("The list is empty")
		else:
			return self.head.data

#returns the last element of data
	def getLast(self):
		if self.length == 0:
			print("The list is empty")
		else:
			currentnode = self.head

			while currentnode.next != None:
				currentnode = currentnode.next
			
			return currentnode.data

#return node at any position
	def getAtPos(self, pos):
		count = 0
        currentnode = self.head
         
        if pos > self.length or pos < 0:
            print "The position does not exist. Please enter a valid position"
        else:
            while currentnode.next != None or count < pos:
                count = count + 1
				if count == pos:
					return currentnode.data
                else:
                    currentnode = currentnode.next
 
                     
    # method to print the whole list
	def print_list(self):
		nodeList = []
        currentnode = self.head
        while currentnode != None:
            nodeList.append(currentnode.data)
            currentnode = currentnode.next 
             
        print nodeList  

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
ll = LinkedList()
ll.addNode(node1)
ll.addNode(node2)
ll.addNode(node3)
ll.addNode(node4)
ll.addNode(node5)
ll.print_list()

					



			
		

		








