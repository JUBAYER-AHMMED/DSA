#include <iostream>
using namespace std;
#define MAX 5
int queue[MAX], front = -1, rear = -1;
int main()
{
  int choice, value;
  while (1)
  {
    cout << "\nQueue Operations:\n";
    cout << "1. Enqueue\n";
    cout << "2. Dequeue\n";
    cout << "3. Display\n";
    cout << "4. Exit\n";
    cout << "Enter your choice: ";
    cin >> choice;
    switch (choice)
    {
    case 1:
      if (rear == MAX - 1)
      {
        cout << "Queue is full! Cannot enqueue.\n";
      }
      else
      {
        if (front == -1)
        {
          front = 0;
        }
        cout << "Enter the value to enqueue: ";
        cin >> value;
        rear++;
        queue[rear] = value;
        cout << value << " enqueued to the queue.\n";
        cout << "Current front: " << front << ", rear: " << rear << endl;
      }
      break;
    case 2:
      if (front == -1 || front > rear)
      {
        cout << "Queue is empty! Cannot dequeue.\n";
      }
      else
      {
        cout << "Dequeued value: " << queue[front] << endl;
        front++;
        cout << "Current front: " << front << ", rear: " << rear << endl;
        if (front > rear)
        {
          front = rear = -1;
          cout << "Queue is now empty.\n";
        }
      }
      break;
    case 3:
      if (front == -1 || front > rear)
      {
        cout << "Queue is empty!\n";
      }
      else
      {
        cout << "Queue elements are: ";
        for (int i = front; i <= rear; i++)
        {
          cout << queue[i] << " ";
        }
        cout << endl;
      }
      break;
    case 4:
      cout << "Exiting...\n";
      return 0;
    default:
      cout << "Invalid choice! Try again.\n";
    }
    if (front == -1 || front > rear)
    {
      cout << "Queue is empty.\n";
    }
    else
    {
      cout << "Current queue: ";
      for (int i = front; i <= rear; i++)
      {
        cout << queue[i] << " ";
      }
      cout << endl;
    }
  }
  return 0;
}