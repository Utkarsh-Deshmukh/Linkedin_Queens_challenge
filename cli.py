import cv2
import linkedin_queens_solver
import click


@click.group()
def cli():
    """A simple CLI application."""
    pass

@click.command
@click.option('--img', prompt="path of image file (unsolved board)", type=str)
def run_example(img):
	image = cv2.imread(img)
	linkedin_queens_solver.solve_queens(image)

cli.add_command(run_example)
if __name__ == '__main__':
    cli()
    
    