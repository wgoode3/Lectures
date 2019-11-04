# HOW DO I ASP.NET CORE?

## Intialize the project

Create a new project (called ```Pandas``` in this case) and <abbr title="change directory">cd</arrb> into it.

```
# assuming you have the dojo template installed
dotnet new dojo -o Pandas
cd Pandas
dotnet add package MySql.Data -v 8.0.16
```

### Adding a database connection

Based on the version of ```dotnet``` you have installed, install the following...

```
# check you dotnet version with...
dotnet --version
```

| Version              | Command                                                            |
|----------------------|--------------------------------------------------------------------|
| 2.1.403              | ```dotnet add package Pomelo.EntityFrameworkCore.MySql -v 2.1.2``` |
| greater than 2.1.403 | ```dotnet add package Pomelo.EntityFrameworkCore.MySql -v 2.1.4``` |

## Modifying our code

Open the project in the text editor of your choice. We should see a folder structure similar to the following...

```
├─ Pandas
  ├─ Controllers
    ├─ HomeController.cs
  ├─ Models
    ├─ MyModel.cs
  ├─ Views
    ├─ Home
      ├─ Index.cshtml
  ├─ appsettings.json
  ├─ Pandas.csproj
  ├─ Startup.cs
  
# some files and folders removed for brevity
```

### Startup.cs changes

Add the following imports at the top of the file.

```csharp
using Microsoft.EntityFrameworkCore;
using Pandas.Models;
```

Next in the ```public void ConfigureServices(...)```...

```csharp
public void ConfigureServices(IServiceCollection services)
{
    services.AddDbContext<PandaContext>(options => options.UseMySql(Configuration["DBInfo:ConnectionString"]));
    services.AddSession();            
    services.AddMvc();
}
```

If using session, in the ```public void Configure(...)``` add the following line...

```csharp
app.UseSession();
```

### Creating the Context Class

In the ```Models``` folder create a file called ```PandaContext.cs```.

Add the following to that file...

```csharp
using Microsoft.EntityFrameworkCore;
using Pandas.Models;

namespace Pandas.Models {
    public class PandaContext : DbContext {
        public PandaContext(DbContextOptions options) : base(options) { }
        public DbSet<Panda> Pandas {get;set;}
    }
}
```

### Creating the Model Class

In the ```Models``` folder create a file called ```Panda.cs``` (or rename ```MyModel.cs```).

Add the following code to that file...

```csharp
using System;
using System.ComponentModel.DataAnnotations;

namespace Pandas.Models
{
    public class Panda
    {
        [Key]
        public int PandaId {get;set;}
        [Required (ErrorMessage = "Panda name is required!")]
        [MinLength(3, ErrorMessage = "Panda name must be 3 characters or more!")]
        public string Name {get;set;}
        [Required (ErrorMessage = "Panda age is required!")]
        [Range(0, 40, ErrorMessage = "Enter a valid panda age!")]
        public int Age {get;set;}
        public DateTime CreatedAt {get;set;} = DateTime.Now;
        public DateTime UpdatedAt {get;set;} = DateTime.Now;
    }
}
```

### Dependency Injecting the Context class into our Controller

Assuming you have renamed ```HomeController.cs``` to ```PandaController.cs```, make sure to add the following at the top of the class...

```csharp

namespace Pandas.Controllers
{
    public class PandaController : Controller
    {
        private PandaContext context;
        
        public PandaController(PandaContext pc)
        {
            context = pc;
        }
        
        // Other Methods ommitted for brevity
    }
}
```

We will create a private field and a constructor to dependency inject ```PandaContext``` into our ```PandaController``` as ```context```.

## Migrations

Before we create the schema and tables in MySQL, we should check out the ```appsettings.json```.

### In appsettings.json

Make sure the ```"ConnectionString"``` contains the correct ```userid```, ```password```, and ```port``` for our database. 
We also can choose our schema name with ```database```. In this case it will be called ```pandadb```.

```js
{
  "Logging": {
    "LogLevel": {
      "Default": "Warning"
    }
  },
  "AllowedHosts": "*",
  "DBInfo": {
    "Name": "MySqlConnection",
    "ConnectionString": "server=localhost;userid=root;password=root;port=3306;database=pandadb;SslMode=None"
  }
}
```

### Making migrations

We can create a migration called ```initial``` with the following command

```
dotnet ef migrations add initial
```

and apply this migration to MySQL with this command

```
dotnet ef database update
```
