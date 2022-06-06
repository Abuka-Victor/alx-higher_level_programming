#include "lists.h"


/**
 * is_palindrome - a function in C that checks
 * if a singly linked list is a palindrome.
 *
 * @head: The head of the linked list
 */
int is_palindrome(listint_t **head)
{
	int count = 0, i, j, *numbers;

	if (!head)
		return (0);

	if (!(*head))
		return (1);

	listint_t *pass = *head, *test = *head;

	for (; pass; pass = pass->next)
		count++;

	numbers = malloc(sizeof(int) * count);

	for (i = 0; test; test = test->next, i++)
		numbers[i] = test->n;

	for (i = 0, j = count - 1; i < count; i++, j--)
	{
		if (numbers[i] != numbers[j])
			return (0);
	}

	return (1);
}
