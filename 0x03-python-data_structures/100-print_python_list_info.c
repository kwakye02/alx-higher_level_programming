#include <Python.h>

/**
 * print_python_list_info – prints the basic info of python lists.
 * @p: PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int  x, size, alloc;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (x = 0; x < size; x++)
	{
		printf("Element %d: ", x);

		obj = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
