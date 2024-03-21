#include <stdio.h>
#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome- checks if a singly linked list is a palindrome
 * 
 * @head: pointer to head- pointer
 * 
 * return 0 if not, or 1 if it is
*/
int is_palindrome(listint_t **head)
{
    listint_t *temp;
    listint_t *traversal;
    listint_t *pre;

    traversal = *head;
    temp = *head;
    pre = *head;

    int palindrome_true = 1;

    while (temp != NULL)
    {
        while(traversal->next != NULL)

        {
            pre = traversal;
            traversal = traversal->next;
            
        }
    

    if (traversal->n != temp->n)
        {
            palindrome_true = 0;
            return palindrome_true;
        }
        temp = temp->next
    }
        return 0;
}