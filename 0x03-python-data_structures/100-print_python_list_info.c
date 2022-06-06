#define PY_SSIZE_T_CLEAN
#include "Python.h"

/**
 * print_python_list_info - a C function that prints some basic info about Python lists.
 * @p: The python object base type
 *
 * Return: Null void
 */
void print_python_list_info(PyObject *p)
{
	int size, i, alloc;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *) p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);

	}
}
