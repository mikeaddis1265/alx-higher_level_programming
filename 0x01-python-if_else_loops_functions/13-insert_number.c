#include "lists.h"
#include "stdlib.h"

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *temp;
    listint_t *temp2 = NULL;
    listint_t *new;

    temp = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
    {
        return NULL;
    }
  
        new->n = number;
        new->next = NULL;

    if (*head == NULL)
    {
        *head = new;
        return *head;
    }
      
    else
    {
        while (temp->next != NULL)
        {
            if (temp->n > number)
            {
                temp2->next = new;
                new->next = temp;
                break;
            }
            temp2 = temp;
            temp = temp->next;
        }
        if (temp->n < number)
        {
            temp->next = new;
            return temp;
        }
        else
        {
            temp2->next = new;
            return temp;
        }
    }
    
    
}
