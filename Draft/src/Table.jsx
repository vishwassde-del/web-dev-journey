import React from 'react'
import './styles.css'

export const Table = () => {
    const employees = [
        { empId: 101, name: 'Alice', dept: 'HR', salary: 50000 },
        { empId: 102, name: 'Bob', dept: 'Engineering', salary: 70000 },
        { empId: 103, name: 'Charlie', dept: 'Sales', salary: 60000 },
        { empId: 104, name: 'David', dept: 'Marketing', salary: 55000 },
    ];
  return (
    <div className='table-container'>
    <table border="1" cellPadding={2} cellSpacing={5} className='employee-table'>
        <tr><thead>
            <th>emp id</th>
            <th>name</th>
            <th>dept</th>
            <th>salary</th>
            </thead>
            <tbody>
            {employees.map((emp) => (
                <tr key={emp.empId}><td>{emp.empId}</td>
                                    <td>{emp.name}</td>
                                    <td>{emp.dept}</td>
                                    <td>{emp.salary}</td>
                </tr>
            ))}
            </tbody>
        </tr>
    </table>
    </div>
  )
}
