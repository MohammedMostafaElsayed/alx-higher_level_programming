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
	if (temp == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
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
	return (NULL);
}
