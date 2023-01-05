#!/usr/bin/python3
""" This defines the class Node"""


class Node:
    """This defines a node of singly linked list

    Args:
       data (int): The value of the node
       next_node (Node): next node of the linked list
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            return self.__data

        @data.setter
        def data(self, value):
            if not isinstance(value, int):
                raise TypeError("data must be an integer")
            self.__data = value

        @property
        def next_node(self):
            return self.__next_node

        @next_node.setter
        def next_node(self, value):
            if value and not isinstance(value, Node):
                raise TypeError("next_node must be a Node object")
            self.__next_node = value


class SinglyLinkedList:
    """This defines a singly linked list

    Args:
      head (Node): This is the start of the linked list
    """
    def __init__(self):
        self.__head = None

    def __str__(self):
        linked_list = ""
        current = self.__head
        while current:
            linked_list += str(current.data)
            linked_list += "\n"
            current = current.next_node
        return linked_list

    def sorted_insert(self, value):
        """ Inserts a new node into the list by increasing order"""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (current.next_node and current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
