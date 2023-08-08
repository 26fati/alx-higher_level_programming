#include "lists.h"
/**
 * insert_node - a function that inserts a number into a,
 * sorted singly linked list.
 * @head: pointer to the head.
 * @number: integer number.
 * Return: returns the address of the new node, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *previous;
	listint_t *current;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	current = (*head)->next;
	previous = *head;
	while (current != NULL)
	{
		if (current->n > number)
			break;
		 current = current->next;
		 previous = previous->next;
	}
	new->next = current;
	previous->next = new;
	return (new);
}
