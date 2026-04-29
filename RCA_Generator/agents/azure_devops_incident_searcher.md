# Azure DevOps Incident Searcher Agent

**Purpose**: Search and extract incident data from Azure DevOps for RCA analysis

## Capabilities

- Search Azure DevOps for specific incidents by ID
- Extract timeline and work item details
- Gather related work items and links
- Export incident data in structured format
- Cross-reference with related PRs and commits

## Tools Available

- WebFetch (for ADO API calls)
- Bash (for az cli commands)
- Grep (for searching ADO exports)
- Read (for analyzing ADO data files)

## Usage

Use this agent when you need to:
- Find incident details in Azure DevOps
- Extract timeline of incident progression
- Gather technical details from work items
- Correlate incidents with code changes

## Configuration

### Authentication
- Uses Azure CLI authentication
- Requires proper ADO permissions
- Can use PAT tokens for API access

### Search Parameters
- **Incident ID**: Primary search parameter
- **Date Range**: Filter by creation/modification date
- **Product Area**: Filter by Tax One, Thomson Reuters products
- **Status**: Active, Resolved, Closed
- **Severity**: Critical, High, Medium, Low

## Example Usage

```bash
# Search for specific incident
az boards work-item show --id INC20260413-2 --org https://dev.azure.com/thomsonreuters

# Search by query
az boards query --wiql "SELECT [System.Id], [System.Title] FROM WorkItems WHERE [System.Title] CONTAINS 'TAX ONE' AND [Microsoft.VSTS.Common.Severity] = 'Critical'"
```

## Output Format

Returns structured data including:
- Work item details
- Timeline of changes
- Related items and dependencies
- Comments and discussions
- Attachment references

## Integration Points

- **Input**: Incident ID or search criteria
- **Output**: Structured incident data for RCA generation
- **Downstream**: Feeds into RCA Generator Agent
- **Related**: Works with Tax One Repository Agent for technical correlation

## Error Handling

- Validates incident ID format
- Handles authentication failures gracefully
- Provides fallback search strategies
- Reports missing or inaccessible incidents

---
**Agent Type**: Incident Data Collector  
**Created**: 14 Apr 2026  
**Version**: 1.0