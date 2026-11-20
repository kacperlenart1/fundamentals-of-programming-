import queue

"""
A queue is a linear data structure that follows
the First In, First Out (FIFO) principle.
This means that the first element added to the queue
will be the first one to be removed. A queue operates
similarly to a real-life queue, such as a line of people
waiting for a service — the person who arrives first
is served first.
"""

# Tworzymy kolejkę.
people = queue.Queue()

# Dodajemy elementy na koniec kolejki.
people.put('Michael')    
people.put('Charlotte')  
people.put('Olivia')     

## Wypisujemy liczbę elementów kolejki.
print('Number of queue elements:', people.qsize())

# Pobieramy i wypisujemy elementy z początku kolejki.
while not people.empty():
    person = people.get()
    print(person)
