#include "lists.h"

/**
 * is_palindrome - Checks if a palindrome.
 * @head: pointer list_int
 *
 * Return: 0 or 1
 */

int is_palindrome(listint_t **head)
{
	listint_t *tmp;
	int val[9999], i = 0, j = 0;

	if ((!*head) || (!head))
	{
		return (1);
	}
	tmp = *head;
	if (!tmp->next)
	{
		return (1);
	}
	while (tmp)
	{
		val[i] = tmp->n;
		tmp = tmp->next;
		i++;
	}
	i--;
	while (i >= 0 && j <= i)
	{
		if (val[i] != val[j])
		{
			return (0);
		}
		i--;
		j++;
	}
	return (1);
}
