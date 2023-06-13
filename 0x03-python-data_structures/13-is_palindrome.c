#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * 
*/
int is_palindrome(listint_t **head)
{
    listint_t *s = *head;
    listint_t *f = *head;
    listint_t *p = NULL;
    listint_t *t;

    while (f != NULL && f->next != NULL) {
        f = f->next->next;
        t = s->next;
        s->next = p;
        p = s;
        s = t;
    }

    if (f != NULL) {
        s = s->next;
    }

    while (s != NULL) {
        if (s->n != p->n) {
            return 0;
        }
        s = s->next;
        p = p->next;
    }

    return 1;
}