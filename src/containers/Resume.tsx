import React from 'react'

// Example of using paths alias via tsconfig.json to easily re-use legacy code
// Also, use TypeScript and JavaScript interchangeably.
import aliasExample from '@myPathAlias/component'

export default () => (
    <div>
        <h1></h1>
        <p>
            React, static sites, performance, speed. It's the stuff that makes us
            tick.
        </p>
        {aliasExample}
    </div>
)

