#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - insert
 * @head: 1 ele
 * @number: 2 ele
 *
 * Return: node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new;

	temp = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (temp == NULL)
	{
		temp = new;
		new->next = NULL;
		return (new);
	}
	while (temp)
	{
		if (number < temp->next->n)
		{
			new->next = temp->next;
			temp->next = new;
			return (new);
		}
		temp = temp->next;
	}
	temp->next = new;
	new->next = NULL;
	return (new);
}
