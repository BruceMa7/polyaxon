# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

from polyaxon.exceptions import PolyaxonConfigurationError
from polyaxon.schemas.polyflow.pipeline import PipelineConfig
from polyaxon.schemas.specs import kinds
from polyaxon.schemas.specs.base import BaseSpecification


class ScheduleSpecificationMixin(object):
    @property
    def schedule(self):
        return self.config.schedule

    @property
    def schedule_kind(self):
        return self.schedule.kind if self.schedule else None

    @property
    def schedule_start_at(self):
        return self.schedule.start_at if self.schedule else None

    @property
    def schedule_end_at(self):
        return self.schedule.end_at if self.schedule else None

    @property
    def schedule_frequency(self):
        return self.schedule.frequency if self.schedule else None

    @property
    def schedule_cron(self):
        return self.schedule.cron if self.schedule else None

    @property
    def schedule_depends_on_past(self):
        return self.schedule.depends_on_past if self.schedule else None

    @property
    def execute_at(self):
        return self.schedule.execute_at if self.schedule else None


class PipelineSpecification(BaseSpecification, ScheduleSpecificationMixin):
    """The polyaxonfile specification for pipelines.

    SECTIONS:
        VERSION: defines the version of the file to be parsed and validated.
        TAGS: defines the tags
        ENVIRONMENT: defines the run environment for experiment.
    """

    _SPEC_KIND = kinds.PIPELINE

    CONFIG = PipelineConfig

    def apply_container_contexts(self, contexts=None):
        raise PolyaxonConfigurationError(
            "This method is not allowed on this specification."
        )

    def apply_context(self):
        self.config.process_dag()
        self.config.validate_dag()
        self.config.process_templates()
        return self