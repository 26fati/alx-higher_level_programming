#include "lists.h"

int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *prev = NULL, *temp;
    listint_t *second_half, *mid = NULL;
    int result = 1;

    if (*head != NULL && (*head)->next != NULL)
    {
        // Use slow and fast pointers to find the middle of the linked list
        while (fast != NULL && fast->next != NULL)
        {
            fast = fast->next->next;
            prev = slow;
            slow = slow->next;
        }

        // If the linked list has odd number of elements, skip the middle node
        if (fast != NULL)
        {
            mid = slow;
            slow = slow->next;
        }

        // Reverse the second half of the linked list
        second_half = slow;
        prev->next = NULL;
        while (second_half != NULL)
        {
            temp = second_half->next;
            second_half->next = slow;
            slow = second_half;
            second_half = temp;
        }

        // Compare the first half and reversed second half
        listint_t *first_half = *head;
        while (slow != NULL)
        {
            if (first_half->n != slow->n)
            {
                result = 0;
                break;
            }
            first_half = first_half->next;
            slow = slow->next;
        }

        // Restore the linked list to its original state
        prev->next = mid;
        while (mid != NULL)
        {
            temp = mid->next;
            mid->next = second_half;
            second_half = mid;
            mid = temp;
        }
    }
    return result;
}
