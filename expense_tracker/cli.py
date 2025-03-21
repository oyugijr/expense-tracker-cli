import argparse
from .commands import (
    AddCommand,
    DeleteCommand,
    ListCommand,
    UpdateCommand,
    SummaryCommand,
    SetBudgetCommand,
)

class CLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(prog='expense-tracker-cli')
        self.subparsers = self.parser.add_subparsers(dest='command', required=True)
        self._setup_commands()

    def _setup_commands(self):

        # CSV_export
        export_parser = self.subparsers.add_parser('export')
        export_parser.add_argument('--output', required=True)
        export_parser.add_argument('--month', type=int, required=False)
        export_parser.add_argument('--category', required=False)

        # budget command
        budget_parser = self.subparsers.add_parser('set-budget')
        budget_parser.add_argument('--month', type=int, required=True)
        budget_parser.add_argument('--amount', type=float, required=True)

        # Add command
        add_parser = self.subparsers.add_parser('add')
        add_parser.add_argument('--description', required=True)
        add_parser.add_argument('--amount', type=float, required=True)
        add_parser.add_argument('--category', required=True) 

        # Delete command
        del_parser = self.subparsers.add_parser('delete')
        del_parser.add_argument('--id', type=int, required=True)

        # Update command
        update_parser = self.subparsers.add_parser('update')
        update_parser.add_argument('--id', type=int, required=True)
        update_parser.add_argument('--description', required=False)
        update_parser.add_argument('--amount', type=float, required=False)
        update_parser.add_argument('--category', required=False)

        # List command
        list_parser = self.subparsers.add_parser('list')
        list_parser.add_argument('--month', type=int, required=False)
        list_parser.add_argument('--category', required=False)

        # Summary command
        summary_parser = self.subparsers.add_parser('summary')
        summary_parser.add_argument('--month', type=int, required=False)
        summary_parser.add_argument('--category', required=False)
        summary_parser.add_argument('--breakdown', action='store_true', required=False)

    def run(self):
        args = self.parser.parse_args()
        
        try:
            if args.command == 'add':
                result = AddCommand(args).execute()
            elif args.command == 'delete':
                result = DeleteCommand(args).execute()
            elif args.command == 'list':
                result = ListCommand(args).execute()
            elif args.command == 'update':
                result = UpdateCommand(args).execute()
            elif args.command == 'summary':
                result = SummaryCommand(args).execute()
            elif args.command == 'set-budget':
                result = SetBudgetCommand(args).execute()
            else:
                raise ValueError("Invalid command")
            
            print(result)
        except Exception as e:
            print(f"Error: {str(e)}")
            exit(1)

if __name__ == '__main__':
    CLI().run()