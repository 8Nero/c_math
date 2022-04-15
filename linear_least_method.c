#include <stdio.h>

double dot_product(double *, double *, int);
double det(double matrix[2][2]);

int countline(char *);

int main() {

	int size;
	double slope, intercept;


	//Count the lines of the data file as a size of the vectors	
	char filename[] = "data";
	FILE *fp;
  	fp = fopen(filename, "r");  
	size = countline(filename);


	double identity_vec[size];
	double x_vec[size], y_vec[size];


	//Initialize the identitiy vector to ones.
	for(int j=0; j<size; j++)
	{
		identity_vec[j] = 1.0;
	}


	//Receive input for the data.
	for(int i=0; i<size; i++)
  {
    fscanf(fp, "%lf %lf\n", &x_vec[i], &y_vec[i]);
  }
	fclose(fp);

	double x_y = dot_product(x_vec, y_vec, size);
	double x_1 = dot_product(x_vec, identity_vec, size);
	double y_1 = dot_product(y_vec, identity_vec, size);
	double id_id = dot_product(identity_vec, identity_vec, size);
	double x_x = dot_product(x_vec, x_vec, size);

	double m1[2][2] = {{x_y, x_1}, 
					   {y_1, id_id}};
	
	double m2[2][2] = {{x_x, x_1},
					   {x_1, id_id}};

	double m3[2][2] = {{x_x, x_y},
					   {x_1, y_1}};

	slope = det(m1)/det(m2);
	intercept = det(m3)/det(m1);

	printf("\nThe best fitting line is:\n");
	printf("slope = %lf\n", slope);
	printf("y-intercept = %lf\n", intercept);
	printf("y = %.4lfx + (%.4lf)\n", slope, intercept);

	
}

double dot_product(double *a, double *b, int size)
{
	double result = 0.0;
	for(int i=0; i<size; i++)
	{
		result += a[i]*b[i];
	}
	return result;
}


double det(double A[2][2])
{
	return (A[0][0]*A[1][1])-(A[0][1]*A[1][0]);
}


int countline(char *filename)

{
  FILE *fp = fopen(filename, "r");
  int c, nl;
  nl = 0;
  while ((c = getc(fp)) != EOF)
    if (c == '\n')
      ++nl;

  fclose(fp);
  return nl;

}