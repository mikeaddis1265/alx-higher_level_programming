#include <stdio.h>
#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * 
 * @head: pointer to head-pointer
 * 
 * return 0 if not, or 1 if it is
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *middle = NULL;
    listint_t *second_half = NULL;
    listint_t *current = NULL;

    if (head == NULL || *head == NULL)
        return 1;

    while (fast != NULL && fast->next != NULL)

        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }
    {
    middle = slow;
    second_half = middle->next;
    middle->next = NULL; // Split the list into two halves

    // Reverse the second half of the list
    current = second_half;
    while (current != NULL)
    {
        listint_t *next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    second_half = prev; // Now, second_half points to the head of the reversed second half

    while (second_half != NULL)
    {
        if (second_half->n != (*head)->n)
            return 0; // If any pair of nodes is not equal, return 0
        second_half = second_half->next;
        *head = (*head)->next; // Move to the next node in the first half
    }

    return 1; // If all pairs of nodes are equal, return 1
}
