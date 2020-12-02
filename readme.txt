Installations:

1. python3
2. pip install django
3. pip install postgresql
4. pip install psycopg2-binary

"json sample of create"
{
	"pizza": {
		"type": "square",
		"size": "large",
		"toppings": "[onion, corn]"
	}
}

"json sample of list"
{
	"pizza": {
        "id":"regular2020-12-02 19:43:15.041629",
        "type":"square",
        "size":"large",
	}
}

"json sample of edit"
{
	"pizza": {
        "id":"regular2020-12-02 19:43:15.041629",
        "operation":"edit",
		"type": "square",
		"toppings": "[onion, corn]"
	}
}