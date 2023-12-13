# Generated by go2rpm 1.9.0
%bcond_without check

%global goipath         github.com/open-telemetry/opentelemetry-collector-contrib
%global gomodulesmode   GO111MODULE=on
Version:                0.91.0

%gometa

%global common_description %{expand:
TODO: some description 
}

%global golicenses      LICENSE cmd/mdatagen/third_party/golint/LICENSE
%global godocs          examples CHANGELOG-API.md CHANGELOG.md\\\
                        CONTRIBUTING.md README.md cmd/configschema/README.md\\\
                        cmd/configschema/docsgen/README.md cmd/configschema/c\\\
                        fgmetadatagen/cfgmetadatagen/README.md\\\
                        cmd/mdatagen/README.md cmd/mdatagen/documentation.md\\\
                        cmd/mdatagen/templates/documentation.md.tmpl\\\
                        cmd/mdatagen/templates/readme.md.tmpl\\\
                        cmd/checkapi/allowlist.txt cmd/githubgen/README.md\\\
                        cmd/githubgen/allowlist.txt\\\
                        cmd/opampsupervisor/README.md\\\
                        cmd/opampsupervisor/specification/README.md\\\
                        cmd/telemetrygen/README.md example\\\
                        exporter/alibabacloudlogserviceexporter/README.md\\\
                        exporter/awscloudwatchlogsexporter/README.md\\\
                        exporter/awsemfexporter/README.md\\\
                        exporter/awskinesisexporter/README.md\\\
                        exporter/awsxrayexporter/README.md\\\
                        exporter/azuremonitorexporter/AUTHENTICATION.md\\\
                        exporter/azuremonitorexporter/README.md\\\
                        exporter/carbonexporter/README.md example\\\
                        exporter/clickhouseexporter/README.md\\\
                        exporter/coralogixexporter/README.md examples\\\
                        exporter/datadogexporter/README.md\\\
                        exporter/dynatraceexporter/README.md\\\
                        exporter/elasticsearchexporter/README.md\\\
                        exporter/f5cloudexporter/README.md\\\
                        exporter/fileexporter/README.md\\\
                        exporter/googlecloudexporter/README.md\\\
                        exporter/googlecloudpubsubexporter/README.md\\\
                        exporter/influxdbexporter/README.md\\\
                        exporter/kafkaexporter/README.md example\\\
                        exporter/loadbalancingexporter/README.md example\\\
                        exporter/logzioexporter/README.md example\\\
                        exporter/lokiexporter/CONTRIBUTING.md\\\
                        exporter/lokiexporter/README.md\\\
                        exporter/opencensusexporter/README.md\\\
                        exporter/prometheusexporter/README.md\\\
                        exporter/prometheusremotewriteexporter/DESIGN.md\\\
                        exporter/prometheusremotewriteexporter/README.md\\\
                        examples exporter/sapmexporter/README.md docs\\\
                        exporter/sentryexporter/README.md example\\\
                        exporter/signalfxexporter/README.md\\\
                        exporter/skywalkingexporter/README.md example\\\
                        exporter/splunkhecexporter/README.md\\\
                        exporter/sumologicexporter/README.md\\\
                        exporter/tanzuobservabilityexporter/README.md example\\\
                        exporter/tencentcloudlogserviceexporter/README.md\\\
                        exporter/zipkinexporter/README.md\\\
                        exporter/alertmanagerexporter/README.md\\\
                        exporter/awss3exporter/README.md\\\
                        exporter/azuredataexplorerexporter/README.md example\\\
                        exporter/cassandraexporter/README.md\\\
                        exporter/datasetexporter/README.md\\\
                        exporter/googlemanagedprometheusexporter/README.md\\\
                        exporter/honeycombmarkerexporter/README.md\\\
                        exporter/instanaexporter/README.md\\\
                        exporter/kineticaexporter/README.md\\\
                        exporter/logicmonitorexporter/README.md example\\\
                        exporter/mezmoexporter/README.md\\\
                        exporter/opensearchexporter/README.md\\\
                        exporter/pulsarexporter/README.md examples\\\
                        exporter/syslogexporter/README.md\\\
                        extension/asapauthextension/README.md\\\
                        extension/awsproxy/README.md\\\
                        extension/basicauthextension/README.md\\\
                        extension/bearertokenauthextension/README.md\\\
                        extension/healthcheckextension/README.md\\\
                        extension/httpforwarder/README.md\\\
                        extension/jaegerremotesampling/README.md\\\
                        extension/oauth2clientauthextension/README.md\\\
                        extension/observer/README.md\\\
                        extension/observer/dockerobserver/README.md\\\
                        extension/observer/ecsobserver/README.md\\\
                        extension/observer/ecstaskobserver/README.md\\\
                        extension/observer/hostobserver/README.md\\\
                        extension/observer/k8sobserver/README.md\\\
                        extension/oidcauthextension/README.md\\\
                        extension/pprofextension/README.md\\\
                        extension/sigv4authextension/README.md\\\
                        extension/sigv4authextension/design.md\\\
                        extension/storage/dbstorage/README.md\\\
                        extension/storage/filestorage/README.md\\\
                        extension/encoding/README.md\\\
                        extension/encoding/jaegerencodingextension/README.md\\\
                        extension/encoding/jsonlogencodingextension/README.md\\\
                        extension/encoding/otlpencodingextension/README.md\\\
                        extension/encoding/textencodingextension/README.md\\\
                        extension/encoding/zipkinencodingextension/README.md\\\
                        extension/headerssetterextension/README.md\\\
                        extension/opampextension/README.md\\\
                        extension/remotetapextension/README.md pkg/README.md\\\
                        pkg/experimentalmetricmetadata/README.md\\\
                        pkg/resourcetotelemetry/README.md\\\
                        pkg/translator/prometheus/README.md\\\
                        pkg/golden/README.md pkg/ottl/CONTRIBUTING.md\\\
                        pkg/ottl/LANGUAGE.md pkg/ottl/README.md\\\
                        pkg/ottl/contexts/README.md\\\
                        pkg/ottl/contexts/ottldatapoint/README.md\\\
                        pkg/ottl/contexts/ottllog/README.md\\\
                        pkg/ottl/contexts/ottlmetric/README.md\\\
                        pkg/ottl/contexts/ottlresource/README.md\\\
                        pkg/ottl/contexts/ottlscope/README.md\\\
                        pkg/ottl/contexts/ottlspan/README.md\\\
                        pkg/ottl/contexts/ottlspanevent/README.md\\\
                        pkg/ottl/ottlfuncs/README.md pkg/pdatatest/README.md\\\
                        docs pkg/stanza/README.md\\\
                        pkg/stanza/fileconsumer/design.md\\\
                        pkg/stanza/operator/input/file/design.md\\\
                        processor/attributesprocessor/README.md\\\
                        processor/cumulativetodeltaprocessor/README.md\\\
                        processor/deltatorateprocessor/README.md\\\
                        processor/filterprocessor/README.md\\\
                        processor/groupbyattrsprocessor/README.md\\\
                        processor/groupbytraceprocessor/README.md\\\
                        processor/k8sattributesprocessor/README.md\\\
                        processor/metricsgenerationprocessor/README.md\\\
                        processor/metricstransformprocessor/README.md\\\
                        processor/probabilisticsamplerprocessor/README.md\\\
                        processor/redactionprocessor/README.md\\\
                        processor/resourcedetectionprocessor/README.md\\\
                        processor/resourceprocessor/README.md\\\
                        processor/routingprocessor/README.md\\\
                        processor/spanmetricsprocessor/README.md\\\
                        processor/spanprocessor/README.md\\\
                        processor/tailsamplingprocessor/README.md\\\
                        processor/transformprocessor/CONTRIBUTING.md\\\
                        processor/transformprocessor/README.md\\\
                        processor/datadogprocessor/README.md\\\
                        processor/logstransformprocessor/README.md\\\
                        processor/remotetapprocessor/README.md\\\
                        processor/schemaprocessor/README.md\\\
                        processor/servicegraphprocessor/README.md\\\
                        processor/sumologicprocessor/README.md\\\
                        receiver/apachereceiver/README.md\\\
                        receiver/apachereceiver/documentation.md\\\
                        receiver/awscontainerinsightreceiver/design.md\\\
                        receiver/awscontainerinsightreceiver/README.md\\\
                        receiver/awsecscontainermetricsreceiver/README.md\\\
                        receiver/awsfirehosereceiver/README.md\\\
                        receiver/awsxrayreceiver/README.md\\\
                        receiver/carbonreceiver/README.md\\\
                        receiver/cloudfoundryreceiver/README.md\\\
                        receiver/collectdreceiver/README.md\\\
                        receiver/couchdbreceiver/README.md\\\
                        receiver/couchdbreceiver/documentation.md\\\
                        receiver/dockerstatsreceiver/README.md\\\
                        receiver/dockerstatsreceiver/documentation.md\\\
                        receiver/elasticsearchreceiver/README.md\\\
                        receiver/elasticsearchreceiver/documentation.md\\\
                        receiver/filelogreceiver/README.md\\\
                        receiver/fluentforwardreceiver/README.md\\\
                        receiver/googlecloudpubsubreceiver/README.md\\\
                        receiver/googlecloudspannerreceiver/README.md\\\
                        receiver/googlecloudspannerreceiver/cardinality.md\\\
                        receiver/hostmetricsreceiver/README.md\\\
                        receiver/influxdbreceiver/README.md\\\
                        receiver/jaegerreceiver/README.md\\\
                        receiver/jmxreceiver/README.md\\\
                        receiver/journaldreceiver/README.md\\\
                        receiver/k8sclusterreceiver/README.md\\\
                        receiver/k8sclusterreceiver/documentation.md\\\
                        receiver/k8seventsreceiver/README.md\\\
                        receiver/kafkametricsreceiver/README.md\\\
                        receiver/kafkametricsreceiver/documentation.md\\\
                        receiver/kafkareceiver/README.md\\\
                        receiver/kubeletstatsreceiver/README.md\\\
                        receiver/kubeletstatsreceiver/documentation.md\\\
                        receiver/memcachedreceiver/README.md\\\
                        receiver/memcachedreceiver/documentation.md\\\
                        receiver/mongodbatlasreceiver/README.md\\\
                        receiver/mongodbatlasreceiver/documentation.md\\\
                        receiver/mongodbreceiver/README.md\\\
                        receiver/mongodbreceiver/documentation.md\\\
                        receiver/mysqlreceiver/README.md\\\
                        receiver/mysqlreceiver/documentation.md\\\
                        receiver/nginxreceiver/README.md\\\
                        receiver/nginxreceiver/documentation.md\\\
                        receiver/opencensusreceiver/README.md\\\
                        receiver/podmanreceiver/README.md\\\
                        receiver/postgresqlreceiver/README.md\\\
                        receiver/postgresqlreceiver/documentation.md\\\
                        receiver/prometheusreceiver/DESIGN.md\\\
                        receiver/prometheusreceiver/README.md\\\
                        receiver/rabbitmqreceiver/README.md\\\
                        receiver/rabbitmqreceiver/documentation.md\\\
                        receiver/receivercreator/README.md\\\
                        receiver/redisreceiver/README.md\\\
                        receiver/redisreceiver/config.md\\\
                        receiver/redisreceiver/documentation.md\\\
                        receiver/riakreceiver/README.md\\\
                        receiver/riakreceiver/documentation.md\\\
                        receiver/sapmreceiver/README.md\\\
                        receiver/signalfxreceiver/README.md examples\\\
                        receiver/simpleprometheusreceiver/README.md\\\
                        receiver/skywalkingreceiver/README.md\\\
                        receiver/splunkhecreceiver/README.md\\\
                        receiver/statsdreceiver/README.md\\\
                        receiver/syslogreceiver/README.md\\\
                        receiver/tcplogreceiver/README.md\\\
                        receiver/udplogreceiver/README.md\\\
                        receiver/wavefrontreceiver/README.md\\\
                        receiver/windowsperfcountersreceiver/README.md\\\
                        receiver/zipkinreceiver/README.md\\\
                        receiver/zookeeperreceiver/README.md\\\
                        receiver/zookeeperreceiver/documentation.md\\\
                        receiver/activedirectorydsreceiver/README.md\\\
                        receiver/activedirectorydsreceiver/documentation.md\\\
                        receiver/aerospikereceiver/README.md\\\
                        receiver/aerospikereceiver/documentation.md\\\
                        receiver/apachesparkreceiver/README.md\\\
                        receiver/apachesparkreceiver/documentation.md\\\
                        receiver/awscloudwatchmetricsreceiver/README.md\\\
                        receiver/awscloudwatchreceiver/README.md\\\
                        receiver/azureblobreceiver/README.md\\\
                        receiver/azureeventhubreceiver/README.md\\\
                        receiver/azuremonitorreceiver/README.md\\\
                        receiver/azuremonitorreceiver/documentation.md\\\
                        receiver/bigipreceiver/README.md\\\
                        receiver/bigipreceiver/documentation.md\\\
                        receiver/chronyreceiver/README.md\\\
                        receiver/chronyreceiver/documentation.md\\\
                        receiver/cloudflarereceiver/README.md\\\
                        receiver/datadogreceiver/README.md\\\
                        receiver/expvarreceiver/README.md\\\
                        receiver/expvarreceiver/documentation.md\\\
                        receiver/filereceiver/README.md\\\
                        receiver/filestatsreceiver/README.md\\\
                        receiver/filestatsreceiver/documentation.md\\\
                        receiver/flinkmetricsreceiver/README.md\\\
                        receiver/flinkmetricsreceiver/documentation.md\\\
                        receiver/gitproviderreceiver/README.md\\\
                        receiver/gitproviderreceiver/documentation.md\\\
                        receiver/haproxyreceiver/README.md\\\
                        receiver/haproxyreceiver/documentation.md\\\
                        receiver/httpcheckreceiver/README.md\\\
                        receiver/httpcheckreceiver/documentation.md\\\
                        receiver/iisreceiver/README.md\\\
                        receiver/iisreceiver/documentation.md\\\
                        receiver/k8sobjectsreceiver/README.md\\\
                        receiver/lokireceiver/README.md\\\
                        receiver/nsxtreceiver/README.md\\\
                        receiver/nsxtreceiver/documentation.md\\\
                        receiver/oracledbreceiver/README.md\\\
                        receiver/oracledbreceiver/documentation.md\\\
                        receiver/otlpjsonfilereceiver/README.md\\\
                        receiver/pulsarreceiver/README.md\\\
                        receiver/purefareceiver/README.md\\\
                        receiver/purefbreceiver/README.md\\\
                        receiver/saphanareceiver/README.md\\\
                        receiver/saphanareceiver/documentation.md\\\
                        receiver/snmpreceiver/README.md\\\
                        receiver/snowflakereceiver/README.md\\\
                        receiver/snowflakereceiver/documentation.md\\\
                        receiver/solacereceiver/README.md\\\
                        receiver/splunkenterprisereceiver/README.md\\\
                        receiver/splunkenterprisereceiver/documentation.md\\\
                        receiver/sqlqueryreceiver/README.md\\\
                        receiver/sqlserverreceiver/README.md\\\
                        receiver/sqlserverreceiver/documentation.md\\\
                        receiver/sshcheckreceiver/README.md\\\
                        receiver/sshcheckreceiver/documentation.md\\\
                        receiver/vcenterreceiver/README.md\\\
                        receiver/vcenterreceiver/documentation.md\\\
                        receiver/webhookeventreceiver/README.md\\\
                        receiver/windowseventlogreceiver/README.md\\\
                        testbed/README.md\\\
                        confmap/provider/s3provider/README.md\\\
                        connector/countconnector/README.md\\\
                        connector/datadogconnector/README.md\\\
                        connector/exceptionsconnector/README.md\\\
                        connector/failoverconnector/README.md\\\
                        connector/routingconnector/README.md\\\
                        connector/servicegraphconnector/README.md\\\
                        connector/spanmetricsconnector/README.md

Name:           opentelemetry-collector-contrib
Release:        1%{?dist}
Summary:        OpenTelemetry Collector Contrib

License:        Apache-2.0 AND BSD-3-Clause AND MIT
URL:            %{gourl}
Source:         %{gosource}

# Patch0: 0001-Update-aliyun-go-sdk-to-0.1.67.patch
Provides: bundled(github.com/open-telemetry/opentelemetry-collector-contrib) = %{version}

Provides: bundled(golang(bitbucket.org/atlassian/go-asap/v2)) = 2.6.0
Provides: bundled(golang(code.cloudfoundry.org/go-loggregator)) = 7.4.0+incompatible
Provides: bundled(golang(github.com/Azure/azure-event-hubs-go/v3)) = 3.6.1
Provides: bundled(golang(github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/monitor/armmonitor)) = 0.11.0
Provides: bundled(golang(github.com/Azure/azure-sdk-for-go/sdk/resourcemanager/resources/armresources)) = 1.2.0
Provides: bundled(golang(github.com/ClickHouse/clickhouse-go/v2)) = 2.15.0
Provides: bundled(golang(github.com/DataDog/opentelemetry-mapping-go/pkg/inframetadata)) = 0.8.1
Provides: bundled(golang(github.com/DataDog/opentelemetry-mapping-go/pkg/otlp/attributes)) = 0.8.3
Provides: bundled(golang(github.com/DataDog/opentelemetry-mapping-go/pkg/otlp/logs)) = 0.8.3
Provides: bundled(golang(github.com/DataDog/opentelemetry-mapping-go/pkg/otlp/metrics)) = 0.8.1
Provides: bundled(golang(github.com/DataDog/opentelemetry-mapping-go/pkg/quantile)) = 0.8.1
Provides: bundled(golang(github.com/GoogleCloudPlatform/opentelemetry-operations-go/detectors/gcp)) = 1.21.0
Provides: bundled(golang(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/collector)) = 0.45.0
Provides: bundled(golang(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/collector)) = 0.45.0
Provides: bundled(golang(github.com/GoogleCloudPlatform/opentelemetry-operations-go/exporter/collector/googlemanagedprometheus)) = 0.45.0
Provides: bundled(golang(github.com/IBM/sarama)) = 1.42.1
Provides: bundled(golang(github.com/ReneKroon/ttlcache/v2)) = 2.11.0
Provides: bundled(golang(github.com/Showmax/go-fqdn)) = 1.0.0
Provides: bundled(golang(github.com/aerospike/aerospike-client-go/v6)) = 6.13.0
Provides: bundled(golang(github.com/alecthomas/participle/v2)) = 2.1.1
Provides: bundled(golang(github.com/aliyun/aliyun-log-go-sdk)) = 0.1.67
Provides: bundled(golang(github.com/cloudfoundry-incubator/uaago)) = 0.0.0
Provides: bundled(golang(github.com/coreos/go-oidc)) = 2.2.1+incompatible
Provides: bundled(golang(github.com/elastic/go-elasticsearch/v7)) = 7.17.10
Provides: bundled(golang(github.com/elastic/go-structform)) = 0.0.10
Provides: bundled(golang(github.com/expr-lang/expr)) = 1.15.6
Provides: bundled(golang(github.com/gosnmp/gosnmp)) = 1.37.0
Provides: bundled(golang(github.com/grafana/loki/pkg/push)) = 0.0.0
Provides: bundled(golang(github.com/influxdata/go-syslog/v3)) = 3.0.1
Provides: bundled(golang(github.com/influxdata/influxdb-observability/common)) = 0.5.8
Provides: bundled(golang(github.com/influxdata/influxdb-observability/influx2otel)) = 0.5.8
Provides: bundled(golang(github.com/influxdata/influxdb-observability/otel2influx)) = 0.5.8
Provides: bundled(golang(github.com/knadh/koanf/v2)) = 2.0.1
Provides: bundled(golang(github.com/mongodb-forks/digest)) = 1.0.5
Provides: bundled(golang(github.com/opensearch-project/opensearch-go/v2)) = 2.3.0
Provides: bundled(golang(github.com/redis/go-redis/v9)) = 9.3.0
Provides: bundled(golang(github.com/relvacode/iso8601)) = 1.3.0
Provides: bundled(golang(github.com/sijms/go-ora/v2)) = 2.7.24
Provides: bundled(golang(github.com/snowflakedb/gosnowflake)) = 1.7.0
Provides: bundled(golang(github.com/tg123/go-htpasswd)) = 1.2.1
Provides: bundled(golang(github.com/tidwall/wal)) = 1.1.7
Provides: bundled(golang(github.com/tilinna/clock)) = 1.1.0
Provides: bundled(golang(github.com/xdg-go/scram)) = 1.1.2
Provides: bundled(golang(go.opentelemetry.io/collector/component)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/config/configauth)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/config/configcompression)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/config/configgrpc)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/config/confighttp)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/config/confignet)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/config/configopaque)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/config/configtelemetry)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/config/configtls)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/confmap)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/connector)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/connector)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/connector/forwardconnector)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/consumer)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/exporter)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/exporter)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/exporter)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/exporter)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/exporter)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/exporter/debugexporter)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/exporter/loggingexporter)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/exporter/otlpexporter)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/exporter/otlphttpexporter)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/extension)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/extension)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/extension)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/extension)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/extension/auth)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/extension/ballastextension)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/extension/zpagesextension)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/featuregate)) = 1.0.0
Provides: bundled(golang(go.opentelemetry.io/collector/otelcol)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/processor)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/processor)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/processor)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/processor/batchprocessor)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/processor/memorylimiterprocessor)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/receiver)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/receiver)) = 0.91.0
Provides: bundled(golang(go.opentelemetry.io/collector/receiver/otlpreceiver)) = 0.91.0
Provides: bundled(golang(gopkg.in/zorkian/go-datadog-api.v2)) = 2.30.0

%description %{common_description}

%prep
%goprep -k
%autopatch -p1

%build
export GOFLAGS="-buildmode=pie"
%undefine gomodulesmode
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE cmd/mdatagen/third_party/golint/LICENSE
%doc examples CHANGELOG-API.md CHANGELOG.md CONTRIBUTING.md README.md
%doc cmd/configschema/README.md cmd/configschema/docsgen/README.md
%doc cmd/configschema/cfgmetadatagen/cfgmetadatagen/README.md
%doc cmd/mdatagen/README.md cmd/mdatagen/documentation.md
%doc cmd/mdatagen/templates/documentation.md.tmpl
%doc cmd/mdatagen/templates/readme.md.tmpl cmd/checkapi/allowlist.txt
%doc cmd/githubgen/README.md cmd/githubgen/allowlist.txt
%doc cmd/opampsupervisor/README.md cmd/opampsupervisor/specification/README.md
%doc cmd/telemetrygen/README.md example
%doc exporter/alibabacloudlogserviceexporter/README.md
%doc exporter/awscloudwatchlogsexporter/README.md
%doc exporter/awsemfexporter/README.md exporter/awskinesisexporter/README.md
%doc exporter/awsxrayexporter/README.md
%doc exporter/azuremonitorexporter/AUTHENTICATION.md
%doc exporter/azuremonitorexporter/README.md exporter/carbonexporter/README.md
%doc example exporter/clickhouseexporter/README.md
%doc exporter/coralogixexporter/README.md examples
%doc exporter/datadogexporter/README.md exporter/dynatraceexporter/README.md
%doc exporter/elasticsearchexporter/README.md exporter/f5cloudexporter/README.md
%doc exporter/fileexporter/README.md exporter/googlecloudexporter/README.md
%doc exporter/googlecloudpubsubexporter/README.md
%doc exporter/influxdbexporter/README.md exporter/kafkaexporter/README.md
%doc example exporter/loadbalancingexporter/README.md example
%doc exporter/logzioexporter/README.md example
%doc exporter/lokiexporter/CONTRIBUTING.md exporter/lokiexporter/README.md
%doc exporter/opencensusexporter/README.md exporter/prometheusexporter/README.md
%doc exporter/prometheusremotewriteexporter/DESIGN.md
%doc exporter/prometheusremotewriteexporter/README.md examples
%doc exporter/sapmexporter/README.md docs exporter/sentryexporter/README.md
%doc example exporter/signalfxexporter/README.md
%doc exporter/skywalkingexporter/README.md example
%doc exporter/splunkhecexporter/README.md exporter/sumologicexporter/README.md
%doc exporter/tanzuobservabilityexporter/README.md example
%doc exporter/tencentcloudlogserviceexporter/README.md
%doc exporter/zipkinexporter/README.md exporter/alertmanagerexporter/README.md
%doc exporter/awss3exporter/README.md
%doc exporter/azuredataexplorerexporter/README.md example
%doc exporter/cassandraexporter/README.md exporter/datasetexporter/README.md
%doc exporter/googlemanagedprometheusexporter/README.md
%doc exporter/honeycombmarkerexporter/README.md
%doc exporter/instanaexporter/README.md exporter/kineticaexporter/README.md
%doc exporter/logicmonitorexporter/README.md example
%doc exporter/mezmoexporter/README.md exporter/opensearchexporter/README.md
%doc exporter/pulsarexporter/README.md examples
%doc exporter/syslogexporter/README.md extension/asapauthextension/README.md
%doc extension/awsproxy/README.md extension/basicauthextension/README.md
%doc extension/bearertokenauthextension/README.md
%doc extension/healthcheckextension/README.md extension/httpforwarder/README.md
%doc extension/jaegerremotesampling/README.md
%doc extension/oauth2clientauthextension/README.md extension/observer/README.md
%doc extension/observer/dockerobserver/README.md
%doc extension/observer/ecsobserver/README.md
%doc extension/observer/ecstaskobserver/README.md
%doc extension/observer/hostobserver/README.md
%doc extension/observer/k8sobserver/README.md
%doc extension/oidcauthextension/README.md extension/pprofextension/README.md
%doc extension/sigv4authextension/README.md
%doc extension/sigv4authextension/design.md
%doc extension/storage/dbstorage/README.md
%doc extension/storage/filestorage/README.md extension/encoding/README.md
%doc extension/encoding/jaegerencodingextension/README.md
%doc extension/encoding/jsonlogencodingextension/README.md
%doc extension/encoding/otlpencodingextension/README.md
%doc extension/encoding/textencodingextension/README.md
%doc extension/encoding/zipkinencodingextension/README.md
%doc extension/headerssetterextension/README.md
%doc extension/opampextension/README.md extension/remotetapextension/README.md
%doc pkg/README.md pkg/experimentalmetricmetadata/README.md
%doc pkg/resourcetotelemetry/README.md pkg/translator/prometheus/README.md
%doc pkg/golden/README.md pkg/ottl/CONTRIBUTING.md pkg/ottl/LANGUAGE.md
%doc pkg/ottl/README.md pkg/ottl/contexts/README.md
%doc pkg/ottl/contexts/ottldatapoint/README.md
%doc pkg/ottl/contexts/ottllog/README.md pkg/ottl/contexts/ottlmetric/README.md
%doc pkg/ottl/contexts/ottlresource/README.md
%doc pkg/ottl/contexts/ottlscope/README.md pkg/ottl/contexts/ottlspan/README.md
%doc pkg/ottl/contexts/ottlspanevent/README.md pkg/ottl/ottlfuncs/README.md
%doc pkg/pdatatest/README.md docs pkg/stanza/README.md
%doc pkg/stanza/fileconsumer/design.md pkg/stanza/operator/input/file/design.md
%doc processor/attributesprocessor/README.md
%doc processor/cumulativetodeltaprocessor/README.md
%doc processor/deltatorateprocessor/README.md
%doc processor/filterprocessor/README.md
%doc processor/groupbyattrsprocessor/README.md
%doc processor/groupbytraceprocessor/README.md
%doc processor/k8sattributesprocessor/README.md
%doc processor/metricsgenerationprocessor/README.md
%doc processor/metricstransformprocessor/README.md
%doc processor/probabilisticsamplerprocessor/README.md
%doc processor/redactionprocessor/README.md
%doc processor/resourcedetectionprocessor/README.md
%doc processor/resourceprocessor/README.md processor/routingprocessor/README.md
%doc processor/spanmetricsprocessor/README.md processor/spanprocessor/README.md
%doc processor/tailsamplingprocessor/README.md
%doc processor/transformprocessor/CONTRIBUTING.md
%doc processor/transformprocessor/README.md processor/datadogprocessor/README.md
%doc processor/logstransformprocessor/README.md
%doc processor/remotetapprocessor/README.md processor/schemaprocessor/README.md
%doc processor/servicegraphprocessor/README.md
%doc processor/sumologicprocessor/README.md receiver/apachereceiver/README.md
%doc receiver/apachereceiver/documentation.md
%doc receiver/awscontainerinsightreceiver/design.md
%doc receiver/awscontainerinsightreceiver/README.md
%doc receiver/awsecscontainermetricsreceiver/README.md
%doc receiver/awsfirehosereceiver/README.md receiver/awsxrayreceiver/README.md
%doc receiver/carbonreceiver/README.md receiver/cloudfoundryreceiver/README.md
%doc receiver/collectdreceiver/README.md receiver/couchdbreceiver/README.md
%doc receiver/couchdbreceiver/documentation.md
%doc receiver/dockerstatsreceiver/README.md
%doc receiver/dockerstatsreceiver/documentation.md
%doc receiver/elasticsearchreceiver/README.md
%doc receiver/elasticsearchreceiver/documentation.md
%doc receiver/filelogreceiver/README.md receiver/fluentforwardreceiver/README.md
%doc receiver/googlecloudpubsubreceiver/README.md
%doc receiver/googlecloudspannerreceiver/README.md
%doc receiver/googlecloudspannerreceiver/cardinality.md
%doc receiver/hostmetricsreceiver/README.md receiver/influxdbreceiver/README.md
%doc receiver/jaegerreceiver/README.md receiver/jmxreceiver/README.md
%doc receiver/journaldreceiver/README.md receiver/k8sclusterreceiver/README.md
%doc receiver/k8sclusterreceiver/documentation.md
%doc receiver/k8seventsreceiver/README.md
%doc receiver/kafkametricsreceiver/README.md
%doc receiver/kafkametricsreceiver/documentation.md
%doc receiver/kafkareceiver/README.md receiver/kubeletstatsreceiver/README.md
%doc receiver/kubeletstatsreceiver/documentation.md
%doc receiver/memcachedreceiver/README.md
%doc receiver/memcachedreceiver/documentation.md
%doc receiver/mongodbatlasreceiver/README.md
%doc receiver/mongodbatlasreceiver/documentation.md
%doc receiver/mongodbreceiver/README.md
%doc receiver/mongodbreceiver/documentation.md receiver/mysqlreceiver/README.md
%doc receiver/mysqlreceiver/documentation.md receiver/nginxreceiver/README.md
%doc receiver/nginxreceiver/documentation.md
%doc receiver/opencensusreceiver/README.md receiver/podmanreceiver/README.md
%doc receiver/postgresqlreceiver/README.md
%doc receiver/postgresqlreceiver/documentation.md
%doc receiver/prometheusreceiver/DESIGN.md receiver/prometheusreceiver/README.md
%doc receiver/rabbitmqreceiver/README.md
%doc receiver/rabbitmqreceiver/documentation.md
%doc receiver/receivercreator/README.md receiver/redisreceiver/README.md
%doc receiver/redisreceiver/config.md receiver/redisreceiver/documentation.md
%doc receiver/riakreceiver/README.md receiver/riakreceiver/documentation.md
%doc receiver/sapmreceiver/README.md receiver/signalfxreceiver/README.md
%doc examples receiver/simpleprometheusreceiver/README.md
%doc receiver/skywalkingreceiver/README.md receiver/splunkhecreceiver/README.md
%doc receiver/statsdreceiver/README.md receiver/syslogreceiver/README.md
%doc receiver/tcplogreceiver/README.md receiver/udplogreceiver/README.md
%doc receiver/wavefrontreceiver/README.md
%doc receiver/windowsperfcountersreceiver/README.md
%doc receiver/zipkinreceiver/README.md receiver/zookeeperreceiver/README.md
%doc receiver/zookeeperreceiver/documentation.md
%doc receiver/activedirectorydsreceiver/README.md
%doc receiver/activedirectorydsreceiver/documentation.md
%doc receiver/aerospikereceiver/README.md
%doc receiver/aerospikereceiver/documentation.md
%doc receiver/apachesparkreceiver/README.md
%doc receiver/apachesparkreceiver/documentation.md
%doc receiver/awscloudwatchmetricsreceiver/README.md
%doc receiver/awscloudwatchreceiver/README.md
%doc receiver/azureblobreceiver/README.md
%doc receiver/azureeventhubreceiver/README.md
%doc receiver/azuremonitorreceiver/README.md
%doc receiver/azuremonitorreceiver/documentation.md
%doc receiver/bigipreceiver/README.md receiver/bigipreceiver/documentation.md
%doc receiver/chronyreceiver/README.md receiver/chronyreceiver/documentation.md
%doc receiver/cloudflarereceiver/README.md receiver/datadogreceiver/README.md
%doc receiver/expvarreceiver/README.md receiver/expvarreceiver/documentation.md
%doc receiver/filereceiver/README.md receiver/filestatsreceiver/README.md
%doc receiver/filestatsreceiver/documentation.md
%doc receiver/flinkmetricsreceiver/README.md
%doc receiver/flinkmetricsreceiver/documentation.md
%doc receiver/gitproviderreceiver/README.md
%doc receiver/gitproviderreceiver/documentation.md
%doc receiver/haproxyreceiver/README.md
%doc receiver/haproxyreceiver/documentation.md
%doc receiver/httpcheckreceiver/README.md
%doc receiver/httpcheckreceiver/documentation.md receiver/iisreceiver/README.md
%doc receiver/iisreceiver/documentation.md receiver/k8sobjectsreceiver/README.md
%doc receiver/lokireceiver/README.md receiver/nsxtreceiver/README.md
%doc receiver/nsxtreceiver/documentation.md receiver/oracledbreceiver/README.md
%doc receiver/oracledbreceiver/documentation.md
%doc receiver/otlpjsonfilereceiver/README.md receiver/pulsarreceiver/README.md
%doc receiver/purefareceiver/README.md receiver/purefbreceiver/README.md
%doc receiver/saphanareceiver/README.md
%doc receiver/saphanareceiver/documentation.md receiver/snmpreceiver/README.md
%doc receiver/snowflakereceiver/README.md
%doc receiver/snowflakereceiver/documentation.md
%doc receiver/solacereceiver/README.md
%doc receiver/splunkenterprisereceiver/README.md
%doc receiver/splunkenterprisereceiver/documentation.md
%doc receiver/sqlqueryreceiver/README.md receiver/sqlserverreceiver/README.md
%doc receiver/sqlserverreceiver/documentation.md
%doc receiver/sshcheckreceiver/README.md
%doc receiver/sshcheckreceiver/documentation.md
%doc receiver/vcenterreceiver/README.md
%doc receiver/vcenterreceiver/documentation.md
%doc receiver/webhookeventreceiver/README.md
%doc receiver/windowseventlogreceiver/README.md testbed/README.md
%doc confmap/provider/s3provider/README.md connector/countconnector/README.md
%doc connector/datadogconnector/README.md
%doc connector/exceptionsconnector/README.md
%doc connector/failoverconnector/README.md connector/routingconnector/README.md
%doc connector/servicegraphconnector/README.md
%doc connector/spanmetricsconnector/README.md
%{_bindir}/*


%changelog
%autochangelog
