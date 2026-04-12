##Projects

###task_00_abc.py

- Create an abstract class named Animal using the ABC package. This class should have an abstract method called sound.
- Create two subclasses of Animal: Dog and Cat. Implement the sound method in each subclass to return the strings “Bark” and “Meow” respectively.

###task_01_duck_typing.py

- Create an abstract class named Shape with two abstract methods: area and perimeter.
- Implement two concrete classes: Circle and Rectangle, both inheriting from - Shape. Each class should provide implementations for the area and perimeter methods.
- Write a standalone function named shape_info that accepts an object of type Shape (by duck typing) and prints its area and perimeter.

###task_02_verboselist.py

Create a class named VerboseList that extends the Python list class. This custom class should print a notification message every time an item is added (using the append or extend methods) or removed (using the remove or pop methods).

- For the append method: After adding the item to the list, print a message like "Added [item] to the list."
- For the extend method: After extending the list, print a message like "Extended the list with [x] items." where [x] is the number of items added.
- For the remove method: Before removing the item from the list, print a message like "Removed [item] from the list."
- For the pop method: Before popping the item from the list, print a message like "Popped [item] from the list." If the index is not specified, default behavior is to pop the last item.

###task_03_countediterator.py

Create a class named CountedIterator that extends the built-in iterator obtained from the iter function. The CountedIterator should keep track of the number of items that have been iterated over. Specifically, you will need to override the __next__ method to increment a counter each time an item is fetched.