"use client";
import React, { useState } from "react";
import { TableComponent } from "nextjs-reusable-table";
import "nextjs-reusable-table/dist/index.css";

interface Props<T> {
  data: T[];
  columns: string[];
  props: (keyof T)[];
}

// export default function GeneTable({data, columns, props}) {
const GeneTable = <T,>({ data, columns, props }: Props<T>) => {
  const [searchTerm, setSearchTerm] = useState("");
//   const [currentPage, setCurrentPage] = useState(1);


  return (
    <div className="w-full">
      <input
        type="text"
        placeholder="Search users..."
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        className="w-full p-2 border rounded-md"
      />
      
      <TableComponent
        columns={columns}
        data={data}
        props={props}
        searchValue={searchTerm}
        // enablePagination
        // page={currentPage}
        // setPage={setCurrentPage}
        // itemsPerPage={5}
      />
    </div>
  );
}

export default GeneTable;