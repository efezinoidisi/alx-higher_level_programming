#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to singly linked list
 * @number: number to be inserted
 *
 * Return: address of new node or NULL if it fails
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *prev = NULL, *node = NULL;

	if (!head || !(*head))
		return (NULL);
	current = *head;

	while (current)
	{
		if (current->n < number)
		{
			prev = current;
			current = current->next;
			continue;
		}
		node = malloc(sizeof(listint_t));
		if (!node)
			return (NULL);
		node->n = number;
		node->next = current;
		if (prev)
			prev->next = node;
		else
			*head = node;
		return (node);
	}
	return (add_nodeint_end(head, number));
}
