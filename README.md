# Boundary API

Get cricket statistics and data via a RESTful API.

## API Endpoints

### Players

#### List All Players

`GET /v1/players`

Query parameters:

- `name` (optional): Filter by player name
- `role` (optional): Filter by playing role
- `national_team` (optional): Filter by national team
- `batting_style` (optional): Filter by batting style
- `bowling_style` (optional): Filter by bowling style

Example:

```
GET /v1/players?name=smith&role=batsman&national_team=australia
```

#### Get Player by ID

`GET /v1/players/{player_id}`

### Series

#### List All Series

`GET /v1/series`

Example:

```
GET /v1/series
```

#### Get Series by ID

`GET /v1/series/{series_id}`

Example:

```
GET /v1/series/456
```

#### Get Series Statistics

`GET /v1/series/{series_id}/stats`

Example:

```
GET /v1/series/456/stats
```

## Features

- Player statistics and information
- Series data and match details
- Multiple API documentation interfaces
- SQLAlchemy integration for database operations
- Type-safe API endpoints with proper validation

## Data Sources

- [Cricsheet](https://cricsheet.org)
- [ESPNCricinfo](https://espncricinfo.com)

## Contributing

We welcome contributions to the Boundary API! Here are some guidelines to help you get started:

### Documentation

- Update the API documentation for any new endpoints
- Add clear docstrings to new functions and classes
- Update the README if necessary

### Pull Request Process

1. Ensure your code is well-tested and documented
2. Update the version number if necessary
3. Submit a pull request with a clear description of the changes
4. Be responsive to feedback and requested changes

### Feature Requests and Bug Reports

- Use the issue tracker to report bugs or request features
- Provide detailed information about the issue or feature request
- Include steps to reproduce for bug reports

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
