#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to linked list
 *
 * Return: 1 if true or 0 if false
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head, *temp = NULL;
	int i, size;

	if (*head == NULL)
		return (1);

	size = get_size(*head);
	i = 0;
	while (current)
	{
		if (i >= size / 2)
			add_nodeint_end(&temp, current->n);
		current = current->next;
		i++;
	}
	temp = reverse_list(temp);
	current = *head;
	while (temp)
	{
		if (temp->n != current->n)
		{
			free_listint(temp);
			return (0);
		}

		current = current->next;
		temp = temp->next;
	}
	free_listint(temp);
	return (1);
}

/**
 * get_size - length of a singly linked list
 * @head: linked list
 *
 * Return: size of list
 */


int get_size(listint_t *head)
{
	int size = 0;

	while (head)
	{
		size++;
		head = head->next;
	}
	return (size);
}


/**
 * reverse_list - reverses a singly linked list
 * @head: singly linked list
 *
 * Return: reversed list
 */

listint_t *reverse_list(listint_t *head)
{
	listint_t *next = NULL, *prev = NULL, *current = head;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	return (prev);
}
