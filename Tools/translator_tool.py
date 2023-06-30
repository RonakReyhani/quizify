from transformers import MarianMTModel, MarianTokenizer
from transformers import Tool

text = """
This paper has been archived. For the latest technical content about this subject, see the AWS Whitepapers & Guides page. Amazon Web Services – AWS Database Migration Service Best Practices is provided for informational purposes only. This document represents AWS’s current product offerings and practices as of the date of issue of this document. Customers are responsible for making their own independent assessment of the information in this document and any use of AWS's products or services. Each of which is provided “as is” without warranty of any kind, whether express or implied. This document does not create any warranties, representations, contractual commitments, conditions or assurances from AWS. The responsibilities and liabilities of AWS to its customers are controlled by AWS agreements. This document is not part of, nor does it modify, any agreement between AWS and its customers. Today, as many companies move database workloads to Amazon Web Services (AWS), they are also interested in changing their primary database engine. This guide explains how to migrate workloads from DMS to VPC. AWS Database Migration Service allows you to migrate data from a source database to a target database. Most current methods for migrating databases to the cloud or switching engines require an extended outage. This paper outlines bestpractices for using AWS DMS. During a migration, the service tracks changes being made on the source database so that they can be applied to the target database. The possible types of migrations are:   Homogenous migrations (migrations between the same engine types) At a high level, when using AWS DMS a user provisions a replication server and defines source and target endpoints. A typical task consists of three major phases: the full load, the application of cached changes, and ongoing replication. Data is loaded from the source database to tables on the target database, eight tables at a time. While the full load is in progress, changes made to the tables that are being loaded are cached on the replication server. The capturing of changes for a given table doesn’t begin until the full load for that table starts. When ALL tables are loaded, you begin to collect changes as transactions for the ongoing replication phase. After all cached changes are applied, your tables are consistent transactionally and you move to the ongoing replication phase, applying changes as transactions. There will be a backlog of transactions causing some lag between the source and target databases. After working through this backlog, the system will eventually reach a steady state. AWS DMS will create the target schema objects that are needed to perform the migration. AWS DMS takes a minimalist approach and creates only those objects required to efficiently migrate the data. In other words, it will create tables, primary keys and in some cases, unique indexes. In most cases, when performing a migration, you will also want to migrate most or all of the source schema. If you are performing a homogeneous migration, use your engine’s native tools to perform a no-data export/import of the  southeasternschema. Any inter-table dependencies, such as foreign key constraints, must be disabled during the “full load” and “cached change application” phases of AWS DMS processing. If your migration is heterogeneous, you can use the AWS Schema Conversion Tool (AWS SCT) to generate a complete target schema for you. AWS DMS is a managed service that runs on an Amazon Elastic Compute Cloud (Amazon EC2) The service connects to the source database, reads the source data, formats the data, and loads the data into the target database. Some of the smaller instance classes are sufficient for testing the service or for small migrations. Large transactions may require some buffering on disk. Cached transactions and log files are also written to disk. Note  T2 type instances are designed to provide moderate baseline performance. If your migration involves a large number of tables, or if you intend to run multiple concurrent replication tasks, you should consider using one of the larger instances. T2 instances are well suited for general purpose workloads, such as web servers, developer environments, and small databases. They are intended for workloads that don't use the full CPU often or consistently, but that occasionally need to burst. Depending on the instance class, your replication server will come with either 50 GB or 100 GB of data storage. This storage is used for log files and any cached changes that are collected. If your source system is busy or takes large transactions, you might need to increase this amount of storage. All storage volumes in AWS DMS are GP2 or General Purpose SSDs. GP2 volumes come with a base performance of three I/O Operations Per Second(IOPS), with abilities to burst up to 3,000 IOPS on a credit basis. Selecting a Multi-AZ instance can protect your migration from storage failures. Most migrations are transient and not intended to run for long periods of time. If you’re using AWS DMS for ongoing replication purposes, selecting a multi-AZ can improve your availability. The change capture process, used when replicating ongoing changes, collects changes from the  database logs by using the database engines native API. Each engine has specific configuration requirements for exposing this change stream to a given user account. Most engines require some additional configuration to make the change data consumable in a meaningful way. For example, Oracle requires the addition of supplemental logging and MySQL requires row-level bin logging. When capturing changes from an Amazon RDS source, ensure backups are enabled and the source is configured to retain change logs for a sufficiently long time. AWS DMS attempts to create the target schema for you, including underlying tables and primary keys. Sometimes this isn’t possible, for example, when the target is Oracle. In MySQL, you have the option through extra connection parameters to have AWS DMS migrate objects to the specified database. Amazon Web Services – AWS Database Migration Service Best Practices. For the purposes of this paper, in Oracle a user and Schema are not synonymous. The following section highlights common and important options to consider when creating a task. This option simply migrates the data from your source system to your target, creating tables as needed. This option performs a full data load while capturing changes on the source. After the full load is complete, captured changes are applied to the target. Replicate data changes only. At that point, you can shut down your applications, let the remaining changes flow through to the target, and restart your applications to point at the target. In some situations it may be more efficient to copy the existing data by using a method outside of AWS DMS. When replicating data changes only, you need to specify a time from which AWS DMS will begin to read changes from the database change logs. It’s important to keep these logs available on the server for a period of time to ensure AWS D MS has access to these changes. By default, AWS DMS will start your task as soon as you create it. In some situations, it’s helpful to postpone the start of the task. This is typically achieved by keeping the logs available for 24 hours (or longer) during the migration process. Target table prep mode tells AWS DMS what to do with tables that already exist. If a table that is a member of a migration doesn’t yet exist on the target, Amazon DMS will create the table. AWS DMS performs these steps when it creates a target table: The source database column data type is converted into an intermediate AWS DMS data type. When the table is created, any data that exists in the target tables is left as is. This can be useful when consolidating data from multiple systems into a single table. The AWS DMS data type is converted into the target data type. This data type conversion is performed for both heterogeneous and homogeneous migrations. For example, in some situations it’s necessary to triple the size of varchar columns to account for multi-byte characters. We recommend going through the AWS DMS documentation on source and target data types to see if all the data types you use are supported. If the resultant data types aren’t to your liking when you’re using AWS DMS to create your objects, you can pre-create those objects on the target database. Large objects (LOBs) require more processing and resources than standard objects. To help with tuning migrations of systems that contain LOBs, AWS DMS offers the following options: Don’t include LOB columns, or full LOB mode.  AWS DMS assumes no information regarding the size of the LOB data. LOBs are migrated in full, in successive pieces, whose size is determined by LOB chunk size. A large LOB chunks size requires more memory and processing. The LOB chunk size should be set to allow AWS DMS to retrieve the majority of LOBs in as few chunks as possible. For example, if you have a table containing three LOBs, and are moving data 1,000 rows at a time, an LOB chunks size of 32 k will require 96,000 k of memory for processing. When limited LOB mode is selected, any LOBs that are larger than  max LOB size are truncated to max LOBSize. Using  limited L OB mode is almost always more efficient and faster than full LOB Mode. LOB columns are transferred only if the source table has a primary key or a unique index on the target table. If you have a table in which most LOBs are small, with a few outliers, it may be a good idea to move them into their own table. The process was designed this way to accommodate the methods source database engines use to manage LOBs. The containing row on the target is created without the LOB data. The table is updated with the L OB data. There are several options for monitoring your tasks using the AWS DMS console. Find appropriate entries in the logs by looking for lines that start with the following. You can use grep (on UNIX-based text editors) or search (for Windows-based editors) to find exactly what you’re looking for. You can find host metrics on your replication instances monitoring tab. Here, you can monitor whether your replication instance is sized appropriately.Replication Task Metrics for replication tasks, including incoming and committed changes, and latency between  the replication host and source/target databases can be found. Individual table metrics can be found under the table statistics tab for each individual task. These metrics include: the number of rows loaded during the full load. The number of inserts, updates, and deletes since the task started. There are a number of factors that will affect the performance of your migration. These include resourceavailability on the source, available network throughput, resource capacity of the replication server, ability of the target to ingest changes, and so on. In our tests, we have been able to migrate a terabyte of data  in approximately 12–13 hours. Our tests were performed using source databases running on EC2, and in Amazon RDS with target databases in RDS. The performance of your migration will be limited by one or more bottlenecks you encounter. The following are a few things you can do to increase performance.Load Multiple Tables in Parallel by default, but increasing this will reduce performance. During the migration, try to remove any processes that would compete for write resources on your target database. This includes disabling unnecessary triggers, validation, secondary indexes, and so on. When migrating to an RDS database, it’s a good idea to disable backups and Multi-AZ on the target until you’re ready to cutover. Using multiple tasks for a single migration can improve performance. If you have sets of tables that don’t participate in common transactions, it may be possible to divide your migration into multiple tasks. Transactional consistency is maintained within a task. Tasks in separate tasks don’t participate in common transactions. Be careful not to put too much stress on the source system. For very large systems or systems with many LOBs, you may also consider using multiple replication servers, each containing one or more tasks. Pay attention to the LOB parameters. Whenever possible, use limited LOB mode. A review of the Amazon Web Services – AWS Database Migration Service Best Practices can help you determine whether this is a good option. If you have a  table which consists of a few large LOBs and mostly smaller L OBs, consider breaking up the table. You can then use a task in limited LOB mode to migrate the table containing small LOBs, and a task  to migrate  the  table containing large Lobs. By default, AWS DMS processes changes in a transactional mode. LOBs are migrated using a two-step process: first, the containing row is created without the LOB, and then the row is updated with the L OB data. Batch optimized apply groups transactions and applies them in batches for efficiency purposes. Using batch optimized apply will almost certainly violate referential integrity constraints. You should disable them during the migration process and enable them as part of the cutover process. During a migration, AWS DMS performs a full table scan of each source table being processed. Each task periodically queries the source for change information. To perform change processing, you may be required to increase the amount of  data written to your database’s change log. Using a read copy will increase the replication lag. If you prefer  not to add load to your source, consider performing the migration from aRead copy of your source system. Amazon Web Services – AWS Database Migration Service Best Practices. Would you like to move your database from a commercial engine to an open source alternative? Maybe you want to move some of your data from RDS into Amazon Redshift. These and other similar scenarios can be considered “Database migrations” A Typical Migration Project includes the following steps. At a  minimum, you’ll want to do the following: Perform an Assessment. Find out what you need to change in your environment to make a migration successful. This is typically an iterative process. The following are  some questions to ask: Which objects do I want to migrate? Are my data types compatible with those covered by AWS DMS? Does my source system have the necessary capacity? It’s a good idea to use a small test migration consisting of a couple of tables to verify you’ve got things properly configured. Test the migration with any objects you suspect could be difficult. These can include LOB objects, character set conversions, complex data types, and so on. You should determine exactly how you intend to migrate your application. The steps can vary dramatically, depending on the type of migration. After you have completed your prototyping, it’s a good idea to test a complete migration. Are all objects accounted for? Does the migration fit within expected time limits? Are there any errors or warnings in the log files that are a concern? How Much Load Will the Migration Process Add to My Source Database? During a migration, AWS DMS performs a full table scan of the source table for each table processed in parallel. To perform change processing, you may be required to increase the amount of  data written to your databases change log. The size, location, and retention of log files can have an impact on the load. If your tasks contain a Change Data Capture (CDC)  component, the size and location of the log file can have a significant impact on load. Total amount of data being migrated, amount and size of LOB data, size of the largest tables, total number of objects being migrated, secondary indexes created on the target before the migration, resources available on the source system, and so on. How Long Does a Typical Database Migration Take?  There is no one formula that will predict how long your migration will take. You can use the free AWS Schema Conversion Tool (AWS SCT) to convert an entire Schema from one database engine to another. All database engines supported by AWS DMS have native tools that you can use to export and import your Schema. The AWS SCT can be used with AWS DMS to facilitate the migration of your entire system. Most of Amazon’s customers should be able to complete a database migration project by themselves. The AWS DMS is intended to be used with one of these methods to perform a complete migration of your database. There are two main reasons we see people switching engines. The customer wants to use a modern framework or platform for their application portfolio. These platforms are available only on more modern database engines. If your project is challenging, or you are short on resources, one of our migration partners should be able to help you. Amazon has tried to make AWS DMS compatible with as many supported database versions as possible. Some database versions don’t support the necessary features required by AWS DMS, especially with respect to change capture and apply. Currently, to fully migrate from an unsupported database engine, you must first upgrade your database to a supported engine. Alternatively, you may be able to perform a complete migration from an “unsupported” version if you don’t need the change capture, and apply capabilities of DMS. Most databases offer a native method for migrating between servers or platforms. If you are performing ahomogeneous migration, one of the following methods might work for you. Amazon Web Services – AWS Database Migration Service Best Practices. Using a simple backup and restore or export/import is the most efficient way to migrate your data. If you’re considering a homogeneous migration, you should first assess whether  a suitable native option exists. In some situations, you might choose to use the native tools to perform the bulk load and use DMS to capture and apply changes. When migrating between different flavors of MySQL or Amazon Aurora, creating and promoting a read replica is most likely your best option. See Importing and Exporting Data From a MySQL DB Instance. If you can successfully set up a replica of your primary database in your target environment by using native tools more easily than you can  with DMS, you should consider using that native method for migrating your system. Some examples include: Myroids, Postgres, Oracle, and SQL Server. This depends on your environment, the distribution of data, and how busy your source system is. The best way to determine whether your particular system is a candidate for DMS is to test it out. Start slowly, to get the configuration worked out, add some complex objects, and finally attempt a full load as a test. Over the course of a weekend (approximately 33 hours) we were able to migrate five terabytes of relatively evenly distributed data. This included four large (250 GB) tables,  a huge (1 TB) table, 1,000 small to moderately sized tables, three tables that contained LOBs varying between 25 GB and 75 GB, and 10,000 very small tables. DMS can be used to help minimize database-related outages when moving a database from outside a VPC into a V PC. Amazon Web Services – AWS Database Migration Service Best Practices. This paper outlines best practices for using AWS DMS to migrate data from a source database to a target database. It also offers answers to several frequently asked questions about migrations. The following are the basic strategies for migrating into a VPC. AWS DMS helps to migrate database workloads to AWS or change database engines while minimizing any associated downtime. Most current methods for migrating databases to the cloud or switching engines require an extended outage. The following individuals and organizations contributed to this document. We are happy to have you as a member of our team. Please share your thoughts in the comments below or email us at jennifer.smith@mailonline.co.uk.
"""


# Step 2: Translate the summary
def translate_text(text, target_lang, source_lang="en", max_chunk_length=512):
    model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)

    # Split the text into smaller chunks
    chunks = [
        text[i : i + max_chunk_length] for i in range(0, len(text), max_chunk_length)
    ]

    translated_text = []

    # Translate each chunk individually
    for chunk in chunks:
        inputs = tokenizer(
            chunk, truncation=True, padding="longest", return_tensors="pt"
        )
        input_ids = inputs.input_ids
        attention_mask = inputs.attention_mask

        translated = model.generate(input_ids=input_ids, attention_mask=attention_mask)

        translated_chunk = tokenizer.batch_decode(translated, skip_special_tokens=True)
        translated_text.extend(translated_chunk)

    return " ".join(translated_text)


# source_lang = "en"
# target_lang = "fr"

# # Step 1: Translate the text
# translated_text = translate_text(text, source_lang, target_lang)
# print(translated_text)


class translate_my_text(Tool):
    name = "translate_text_tool"
    description = "This is a tool for translating a text file content. It takes two inputs, first the file content as text, then the target language. It translates the content and returns the result as text"
    input = ["text", "text"]
    output = ["audio"]

    def __call__(self, txt: str, target_lang: str):
        return translate_text(txt, target_lang)


translate_text_tool = translate_my_text()
