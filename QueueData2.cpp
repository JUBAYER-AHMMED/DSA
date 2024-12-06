#include <iostream>
#define SIZE 100 // Define a fixed size for the queue

using namespace std;

class Queue
{
private:
  int arr[SIZE]; // Array to store queue elements
  int front;     // Index of the front element
  int rear;      // Index of the rear element
  int count;     // Count of elements in the queue

public:
  // Constructor to initialize the queue
  Queue() : front(0), rear(-1), count(0) {}

  // Enqueue operation: Add an element to the rear of the queue
  void enqueue(int item)
  {
    if (isFull())
    {
      cout << "Queue is full. Cannot enqueue " << item << "." << endl;
      return;
    }
    rear = (rear + 1) % SIZE; // Circular increment
    arr[rear] = item;
    count++;
    cout << "Enqueued: " << item << endl;
  }

  // Dequeue operation: Remove and return the front element of the queue
  int dequeue()
  {
    if (isEmpty())
    {
      cout << "Queue is empty. Cannot dequeue." << endl;
      return -1; // Indicating failure
    }
    int item = arr[front];
    front = (front + 1) % SIZE; // Circular increment
    count--;
    return item;
  }

  // Peek operation: Return the front element without removing it
  int peek()
  {
    if (isEmpty())
    {
      cout << "Queue is empty. No front element." << endl;
      return -1; // Indicating failure
    }
    return arr[front];
  }

  // Check if the queue is empty
  bool isEmpty()
  {
    return count == 0;
  }

  // Check if the queue is full
  bool isFull()
  {
    return count == SIZE;
  }

  // Display the contents of the queue
  void display()
  {
    if (isEmpty())
    {
      cout << "Queue is empty." << endl;
      return;
    }
    cout << "Queue: ";
    for (int i = 0; i < count; i++)
    {
      cout << arr[(front + i) % SIZE] << " ";
    }
    cout << endl;
  }
};

int main()
{
  Queue queue;

  queue.enqueue(10);
  queue.enqueue(20);
  queue.enqueue(30);

  queue.display();

  cout << "Front element: " << queue.peek() << endl;

  cout << "Dequeued: " << queue.dequeue() << endl;
  queue.display();

  cout << "Dequeued: " << queue.dequeue() << endl;
  cout << "Dequeued: " << queue.dequeue() << endl;
  queue.dequeue(); // Attempt to dequeue from an empty queue

  queue.display();

  return 0;
}
