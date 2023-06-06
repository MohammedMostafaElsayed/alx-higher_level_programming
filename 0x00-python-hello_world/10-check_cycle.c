#include "lists.h"

/**
 * check_cycle - check the cycle
 * @list: 1 arg
 *
 * Return: int
 */
int check_cycle(listint_t *list)
{
	listint_t *f, *s;

	f = list->next;
	s = list;
	if (f == NULL || s == NULL)
		return (0);
	while (s != f)
	{
		if (f == NULL || f->next == NULL)
			return (0);
		f = f->next->next;
		s = s->next;
	}
	return (1);
}
