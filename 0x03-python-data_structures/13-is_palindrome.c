#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: linked list
 *
 * Return: 1 if true or 0 if false
 */

int is_palindrome(listint_t **head)
{
	int i;

	if (head == NULL)
		return (1);

	i = palindrome_helper(*head);

	return (i);
}

/**
 * palindrome_helper - checks if a singly linked list is a palindrome
 * @head: start of linked list
 *
 * Return: 1 if true or 0 if false
 */


int palindrome_helper(listint_t *head)
{
	int *arr;
	int i, j, temp, len;
	listint_t *current;

	current = head;
	len = 0;
	arr = malloc(sizeof(int) * len);
	if (arr == NULL)
		return (0);
	while (current)
	{
		arr[i] = current->n;
		len++;
		i++;
		current = current->next;
	}
	arr[i] = 0;
	/* reverse the array */
	for (i = 0, j = len - 1; i < len / 2; i++, j--)
	{
		temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}
	/* compare linked list with reversed array */
	current = head;
	for (i = 0; current; i++)
	{
		if (current->n != arr[i])
		{
			free(arr);
			return (0);
		}
		current = current->next;
	}
	free(arr);
	return (1);
}
