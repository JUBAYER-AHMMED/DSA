#include <bits/stdc++.h>
using namespace std;
#define SIZE 100

class Queue
{
private:
  int a[SIZE];
  int front;
  int rear;
  int count;

public:
  Queue() : front(0), rear(-1), count(0) {}

  void enqueue(int item)
  {
    if (isFull())
    {
      cout << "Queue is full. Cannot enqueue " << item << " .\n";
      return;
    }
    rear = (rear + 1) % SIZE;
    a[rear] = item;
    count++;
    cout << "Enqueued : " << item << endl;
  }

  void dequeue()
  {
    if (isEmpty())
    {
      cout << "Queue is empty. Cannot dequeue . " << endl;
      return; // indicating failure.
    }
    int item = a[front];
    front = (front + 1) % SIZE;
    count--;
    cout << "Dequeued : " << item << endl;
  }

  int peak()
  {
    if (isEmpty())
    {
      cout << "Queue is empty. No front element.\n";
      return -1;
    }
    return a[front];
  }

  bool isEmpty()
  {
    return count == 0;
  }
  bool isFull()
  {
    return count == SIZE;
  }

  void display()
  {
    if (isEmpty())
    {
      cout << "Queue is empty.\n";
      return;
    }
    cout << "Queue : ";
    for (int i = 0; i < count; i++)
    {
      cout << a[(front + i) % SIZE] << " ";
    }
    cout << endl;
  }
};
int main()
{
  Queue Q;
  Q.enqueue(10);
  Q.enqueue(20);
  Q.enqueue(30);
  Q.display();

  cout << "Front element : " << Q.peak() << endl;

  Q.dequeue();
  Q.display();
  Q.dequeue();
  Q.dequeue();
  Q.dequeue();

  Q.display();

  return 0;
}
