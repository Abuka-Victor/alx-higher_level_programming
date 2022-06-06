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
	listint_t *pass, *test;

	if (!head)
		return (0);

	if (!(*head))
		return (1);

	pass = test = *head;

	for (; pass; pass = pass->next)
		count++;

	numbers = malloc(sizeof(int) * count);

	for (i = 0; test; test = test->next, i++)
		numbers[i] = test->n;

	for (i = 0, j = count - 1; i < count; i++, j--)
	{
		if (numbers[i] != numbers[j])
		{
			free(numbers);
			return (0);
		}
	}

	free(numbers);
	return (1);
}
