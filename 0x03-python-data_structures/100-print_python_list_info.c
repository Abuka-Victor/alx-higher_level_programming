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
	Py_ssize_t listSize = PyList_Size(p);
	printf("[*] Size of the Python List = %d", listSize);
}
