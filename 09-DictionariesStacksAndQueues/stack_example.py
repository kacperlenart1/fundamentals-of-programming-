import queue

"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle.
This means the last element added to the stack
is the first one to be removed. Think of a stack
as a pile of plates — the last plate you place
on the top is the first one you'll take off.
"""

# Tworzymy stos.
cards = queue.LifoQueue()

# Dodajemy elementy na wierzch stosu.
cards.put('King of Hearts \u2665')    
cards.put('Queen of Diamonds \u2666')  
cards.put('Jack of Spades \u2660')     

## Wypisujemy liczbę elementów stosu.
print('Number of stack elements:', cards.qsize())

# Zdejmujemy i wypisujemy elementy z wierzchu stosu.
while not cards.empty():
    card = cards.get()
    print(card)

"""
Note the order of the printed elements.
The last added element is printed first.
"""
