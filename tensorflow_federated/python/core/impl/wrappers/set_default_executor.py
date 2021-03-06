# Lint as: python3
# Copyright 2018, The TensorFlow Federated Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""A utility to change the default executor."""

from tensorflow_federated.python.core.impl import context_stack_impl
from tensorflow_federated.python.core.impl import execution_context
from tensorflow_federated.python.core.impl import executor_factory


def set_default_executor(executor_factory_instance=None):
  """Places an `executor`-backed execution context at the top of the stack.

  Args:
    executor_factory_instance: An instance of
      `executor_factory.ExecutorFactory`, or `None` for the default executor.
  """
  if executor_factory_instance is None:
    context = None
  elif isinstance(executor_factory_instance, executor_factory.ExecutorFactory):
    context = execution_context.ExecutionContext(executor_factory_instance)
  else:
    raise TypeError(
        '`set_default_executor` expects either an '
        '`executor_factory.ExecutorFactory` or `None` for the '
        'default context; you passed an argument of type {}.'.format(
            type(executor_factory_instance)))
  context_stack_impl.context_stack.set_default_context(context)
