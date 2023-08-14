#include "lists.h"

/**
 * reverse_listint - Reverses a listint_t list.
 * @head: A pointer to the address of
 *        the head of the list_t list.
 *
 * Return: A pointer to the first node of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
        listint_t *previous = NULL, *current;

        if (*head == NULL)
                return (NULL);
        while (*head != NULL)
        {
                current = (*head)->next;
                (*head)->next = previous;
                previous = *head;
                *head = current;
        }
        (*head) = previous;
        return (*head);
}


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
	listint_t *first_start, *second_start;
	listint_t *p, *q;

	p = *head;
	q = *head;
	if (p->next == NULL || p == NULL)
		return (1);
	while (1)
	{
		p = p->next->next;
		if (p == NULL)
		{
			second_start = q->next;
			break;
		}
		if (p->next == NULL)
		{
			second_start = q->next->next;
			break;
		}
		q = q->next;
	}
	q->next = NULL;
	first_start = *head;
	reverse_listint(&second_start);
	while (first_start && second_start)
	{
		if (first_start->n == second_start->n)
		{
			first_start = first_start->next;
			second_start = second_start->next;
		}
		else
			return (0);
	}
	return (1);

}
