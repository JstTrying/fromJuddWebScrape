from query_manager import QueryManager
from csv_manager import CSVManager

if __name__ == '__main__':
    keyword = input("Search: ")
    print("Please wait... Retrieving results...")
    print("This might take a minute or two...")
    print("\n")
    manager = QueryManager(keyword=keyword)
    manager.start()
    print("Found Results: " + str(manager.current_index))
    CSVManager(keyword, manager.get_entries()).save()

