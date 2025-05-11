## RETRIEVER IN ACTION
```powershell
PS C:\Users\harsh\Desktop\RAG-a-Doodle-Doo> python retriever.py
Usage: python retriever.py [rebuild|query] ["your query"]

PS C:\Users\harsh\Desktop\RAG-a-Doodle-Doo> python retriever.py rebuild 
Batches: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  1.04it/s]
[+] FAISS index saved to data\index.faiss
[+] Metadata saved to data\metadata.npy

PS C:\Users\harsh\Desktop\RAG-a-Doodle-Doo> python retriever.py query "What is the difference between lists and dictionaries?"
[0.7154] doc4.txt#0: Python offers several built-in data structures for storing collections of data. - Lists: Ordered, mutable sequences. Example: [1, 2, 3] - Tuples: Ordered, immutable sequences. Example: (1, 2, 3) - Sets: Unordered, unique elements. Example: {1, 2, 3} - Dictionaries: Key-value pairs. Example: {"name": "Alice", "age": 25} You can access list elements using indices. Dictionary values are accessed using keys. Sets support operations like union and intersection. Each data structure serves different purposes based on the requirements of the program.
[0.5284] doc1.txt#0: Python is a popular programming language known for its readability and ease of use. It uses indentation to define code blocks instead of curly braces. Python supports both object-oriented and functional programming styles. Variables in Python are dynamically typed, meaning you don’t have to declare their type explicitly. For example: x = 10 name = "Alice" Python has several built-in data types such as integers, floats, strings, and booleans. The `type()` function can be used to check the data type of a variable. Comments are written using the hash symbol (#), and Python files use the `.py` extension.
[0.4577] doc3.txt#0: Functions in Python are defined using the `def` keyword. A function may take arguments and may return a value using the `return` statement. Example: def greet(name): return "Hello " + name Python supports default arguments and keyword arguments. Functions help modularize code and reduce repetition. Function scope determines which variables are accessible. Variables defined inside a function are local to that function unless declared global.
```

## DEMO OUTPUT

Question: what are features of python

> Branch: RAG

Retrieved Context:
 - [0.6711] doc1.txt#0: Python is a popular programming language known for its readability and ease of use. It uses indentat...
 - [0.6351] doc4.txt#0: Python offers several built-in data structures for storing collections of data. - Lists: Ordered, mu...
 - [0.6029] doc3.txt#0: Functions in Python are defined using the `def` keyword. A function may take arguments and may retur...

Answer:
Based on the provided information, the following are features of Python:

1. **Readability and ease of use**
2. **Indentation-based code blocks** (instead of curly braces)
3. **Support for object-oriented and functional programming styles**
4. **Dynamically typed variables** (no need to declare type explicitly)
5. **Built-in data types**: integers, floats, strings, booleans
6. **Built-in data structures**: Lists, Tuples, Sets, Dictionaries
7. **Functions**: defined using `def` keyword, can take arguments, return values, support default and keyword arguments
8. **Modular code**: functions reduce repetition and improve code structure
10. **Function scope**: determines which variables are accessible
11. **Comments**: written using the hash symbol (#)
12. **File extension**: `.py`

Let me know if you'd like me to clarify or expand on any of these features!


Question: tell me more about built in data structures

> Branch: RAG

Retrieved Context:
 - [0.7285] doc4.txt#0: Python offers several built-in data structures for storing collections of data. - Lists: Ordered, mu...
 - [0.5287] doc1.txt#0: Python is a popular programming language known for its readability and ease of use. It uses indentat...
 - [0.4274] doc3.txt#0: Functions in Python are defined using the `def` keyword. A function may take arguments and may retur...

Answer:
According to the provided information, Python offers several built-in data structures for storing collections of data, which are:

1. **Lists**: Ordered, mutable sequences. Example: `[1, 2, 3]`. You can access list elements using indices.

2. **Tuples**: Ordered, immutable sequences. Example: `(1, 2, 3)`.

3. **Sets**: Unordered, unique elements. Example: `{1, 2, 3}`. Sets support operations like union and intersection.

4. **Dictionaries**: Key-value pairs. Example: `{"name": "Alice", "age": 25}`. Dictionary values are accessed using keys.

Each data structure serves different purpose based on the requirements of the program.


Question: exit
