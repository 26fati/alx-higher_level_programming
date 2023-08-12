#include "lists.h"
int is_palindrome(listint_t **head)
{
	listint_t *ptr;
	int len, index = 0;
	
	len = findlength(head);
	int arr[len];
	ptr = *head;
	while(ptr)
	{
		arr[index++] = ptr->n;
		ptr = ptr->next;
	}
	for (index = 0; index < (len / 2); index++)
	{
		if (arr[index] != arr[len-index-1])
		{
			return (0);
		}
	}
	return (1);
}
int findlength(listint_t **head)
{
	listint_t *curr;
	int count = 0;

	curr = *head;
	while(curr)
	{
		count++;
		curr = curr->next;
	}
	return (count);
}
