#include "lists.h"

/**
 * is_palindrome - a function in C that checks
 * if a singly linked list is a palindrome.
 *
 * @head: a head of list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr;
	int len, index = 0;

	len = findlength(head);
	int arr[len];

	ptr = *head;

	while (ptr)
	{
		arr[index++] = ptr->n;
		ptr = ptr->next;
	}
	for (index = 0; index < (len / 2); index++)
	{
		if (arr[index] != arr[len - index - 1])
		{
			return (0);
		}
	}
	return (1);
}

/**
 * findlength - a function that find the length of the list.
 *
 * @head: the head of the list.
 *
 * Return: return the length of the list.
 */
int findlength(listint_t **head)
{
	listint_t *curr;
	int count = 0;

	curr = *head;
	while (curr)
	{
		count++;
		curr = curr->next;
	}
	return (count);
}
